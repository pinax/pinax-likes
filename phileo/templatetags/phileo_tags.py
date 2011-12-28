from django import template
from django.conf import settings
from django.core.urlresolvers import reverse

from django.template.loader import render_to_string
from django.contrib.contenttypes.models import ContentType

from phileo.models import Like
from phileo.utils import _allowed, LIKABLE_MODELS

register = template.Library()


class LikesNode(template.Node):
    
    def __init__(self, user, model_list, varname):
        self.user = template.Variable(user)
        
        # Default to all the registered models
        if len(model_list) == 0:
            # These need to look like strings, otherwise they will be treated as variables
            # when they are `resolve()`d later
            model_list = ['"%s"' % model for model in LIKABLE_MODELS]
        
        self.model_list = [template.Variable(m) for m in model_list]
        self.varname = varname
    
    def render(self, context):
        user = self.user.resolve(context)
        content_types = []
        
        for raw_model_name in self.model_list:
            try:
                model_name = raw_model_name.resolve(context)
            except template.VariableDoesNotExist:
                continue
            
            if not _allowed(model_name):
                continue
            
            app, model = model_name.split(".")
            content_type = ContentType.objects.get(app_label=app, model__iexact=model)
            content_types.append(content_type)
        
        context[self.varname] = Like.objects.filter(
            sender=user,
            receiver_content_type__in=content_types
        )
        return ""


@register.tag
def likes(parser, token):
    """
    {% likes user "app.Model" "app.Model" "app.Model" as like_objs %}
    """
    tokens = token.split_contents()
    user = tokens[1]
    varname = tokens[-1]
    model_list = tokens[2:-2]
    
    return LikesNode(user, model_list, varname)


class LikeRenderer(template.Node):
    
    def __init__(self, varname):
        self.varname = template.Variable(varname)
    
    def render(self, context):
        like = self.varname.resolve(context)
        
        instance = like.receiver
        content_type = like.receiver_content_type
        app_name = content_type.app_label
        model_name = content_type.model.lower()
        
        like_context = {
            'instance': instance,
            'like': like,
        }
        
        return render_to_string([
            'phileo/%s/%s.html' % (app_name, model_name),
            'phileo/%s/like.html' % (app_name),
            'phileo/_like.html',
        ], like_context, context)


@register.tag
def render_like(parser, token):
    """
    {% likes user as like_list %}
    <ul>
        {% for like in like_list %}
            <li>{% render_like like %}</li>
        {% endfor %}
    </ul>
    """
    
    tokens = token.split_contents()
    var = tokens[1]
    
    return  LikeRenderer(var)


@register.filter
def likes_count(obj):
    """
    Something like:
    
        <div class="likes_count">{{ obj|likes_count }}</div>
    
    will render:
    
        <div class="likes_count">34</div>
    """
    return Like.objects.filter(
        receiver_content_type=ContentType.objects.get_for_model(obj),
        receiver_object_id=obj.pk
    ).count()


@register.inclusion_tag("phileo/_css.html")
def phileo_css():
    return {"STATIC_URL": settings.STATIC_URL}


@register.inclusion_tag("phileo/_js.html")
def phileo_js():
    return {"STATIC_URL": settings.STATIC_URL}


@register.inclusion_tag("phileo/_widget_js.html")
def phileo_widget_js(user, obj, widget_id=None, like_type="like", toggle_class="phileo-liked"):
    ct = ContentType.objects.get_for_model(obj)
    
    if widget_id == None:
        widget_id = "phileo_%s_%s_%s" % (like_type, ct.pk, obj.pk)
    
    like_count_id = "%s_count" % widget_id
    
    return {
        "user": user,
        "widget_id": widget_id,
        "like_count_id": like_count_id,
        "toggle_class": toggle_class
    }


@register.inclusion_tag("phileo/_widget.html")
def phileo_widget(user, obj, like_text="Like|Unlike", counts_text="like|likes", widget_id=None, like_type="like", toggle_class="phileo-liked"):
    ct = ContentType.objects.get_for_model(obj)
    
    if "|" in like_text:
        like_text = like_text.split("|")
    else:
        like_text = ("Like", "Unlike")
    
    if "|" in counts_text:
        counts_text = counts_text.split("|")
    else:
        counts_text = ("like", "likes")
    
    like_count = Like.objects.filter(
       receiver_content_type = ct,
       receiver_object_id = obj.pk
    ).count()
    
    if widget_id == None:
        widget_id = "phileo_%s_%s_%s" % (like_type, ct.pk, obj.pk)
    
    like_count_id = "%s_count" % widget_id
    
    if user.is_anonymous():
        liked = False
        like_url = settings.LOGIN_URL
    else:
        like_url = reverse("phileo_like_toggle", kwargs={
            "content_type_id": ct.id,
            "object_id": obj.pk
        })
        liked = Like.objects.filter(
           sender = user,
           receiver_content_type = ct,
           receiver_object_id = obj.pk
        ).exists()
    
    return {
        "user": user,
        "like_url": like_url,
        "widget_id": widget_id,
        "like_type": like_type,
        "like_count": like_count,
        "like_count_id": like_count_id,
        "toggle_class": toggle_class,
        "is_liked": toggle_class if liked else "",
        "counts_text": counts_text,
        "like_text": like_text
    }


class LikedObjectsNode(template.Node):
    
    def __init__(self, objects, user, varname):
        self.objects = template.Variable(objects)
        self.user = template.Variable(user)
        self.varname = varname
    
    def get_objects(self, user, objects):
        is_stream = None
        get_id = None
        indexed = {}
        
        for obj in objects:
            if hasattr(obj, "cast") and callable(obj.cast):
                obj = obj.cast()
            if is_stream is None and get_id is None:
                is_stream = not hasattr(obj, "_meta")
                get_id = lambda x: is_stream and x.item.id or x.id
            
            ct = ContentType.objects.get_for_model(is_stream and obj.item or obj)
            if ct not in indexed.keys():
                indexed[ct] = []
            obj.liked = False
            indexed[ct].append(obj)
        
        for ct in indexed.keys():
            likes = Like.objects.filter(
                sender=user,
                receiver_content_type=ct,
                receiver_object_id__in=[get_id(o) for o in indexed[ct]]
            )
            
            for obj in indexed[ct]:
                for like in likes:
                    if like.receiver_object_id == get_id(obj):
                        obj.liked = True
                yield obj
    
    def render(self, context):
        user = self.user.resolve(context)
        objects = self.objects.resolve(context)
        context[self.varname] = self.get_objects(user, objects)
        return ""


@register.tag
def liked(parser, token):
    """
    {% liked objects by user as varname %}
    """
    tag, objects, _, user, _, varname = token.split_contents()
    return LikedObjectsNode(objects, user, varname)
