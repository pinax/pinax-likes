from django import template
from django.core.urlresolvers import reverse

from django.contrib.contenttypes.models import ContentType

from phileo.models import Like


register = template.Library()


class LikesNode(template.Node):
    
    def __init__(self, user, model_list, varname):
        self.user = template.Variable(user)
        self.model_list = [template.Variable(m) for m in model_list]
        self.varname = varname
    
    def render(self, context):
        user = self.user.resolve(context)
        content_types = []
        for model_name in self.model_list:
            app, model = model_name.resolve(context).split(".")
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


@register.inclusion_tag("phileo/_ajax.js")
def likes_ajax():
    return {}


@register.inclusion_tag("phileo/_form.html")
def like_form(user, obj, labels):
    """
    {% like_form user object "like,unlike" %}
    
    This renders a form with a single button that is like
    or unlink based on the current state.
    
    The labels string should be two choices separated by a
    single comma, where the first is the positive choice,
    and the second is the negating choice.
    """
    choices = labels.split(",")
    ct = ContentType.objects.get_for_model(obj)
    qs = Like.objects.filter(
        sender = user,
        receiver_content_type = ct,
        receiver_object_id = obj.pk
    )
    if qs.exists():
        current = choices[1]
        opposite = choices[0]
    else:
        current = choices[0]
        opposite = choices[1]
    
    link_url = reverse("phileo_like_toggle", kwargs={
        "pk": user.id,
        "content_type_id": ct.pk,
        "object_id": obj.pk
    })
    
    return {
        "like_url": link_url,
        "current": current,
        "opposite": opposite
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
