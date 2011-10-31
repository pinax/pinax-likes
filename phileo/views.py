from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

from django.http import HttpResponse
from django.utils import simplejson as json
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from phileo.models import Like
from phileo.signals import object_liked, object_unliked


@require_POST
@login_required
def like_toggle(request, content_type_id, object_id):
    content_type = get_object_or_404(ContentType, pk=content_type_id)
    
    like, created = Like.objects.get_or_create(
        sender = request.user,
        receiver_content_type = content_type,
        receiver_object_id = object_id
    )
    
    if created:
        object_liked.send(sender=Like, like=like)
    else:
        like.delete()
        object_unliked.send(
            sender=Like,
            object=content_type.get_object_for_this_type(
                pk=object_id
            )
        )
    
    if request.is_ajax():
        return HttpResponse(json.dumps({
            "likes_count": Like.objects.filter(
                receiver_content_type = content_type,
                receiver_object_id = object_id
            ).count()
        }), mimetype="application/json")
    
    return redirect(request.META["HTTP_REFERER"])
