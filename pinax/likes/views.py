import json

from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

from .models import Like
from .signals import object_liked, object_unliked
from .utils import widget_context


@login_required
@require_POST
def like_toggle(request, content_type_id, object_id):
    content_type = get_object_or_404(ContentType, pk=content_type_id)
    obj = content_type.get_object_for_this_type(pk=object_id)

    if not request.user.has_perm("likes.can_like", obj):
        return HttpResponseForbidden()

    like, liked = Like.like(request.user, content_type, object_id)

    if liked:
        object_liked.send(sender=Like, like=like, request=request)
    else:
        object_unliked.send(sender=Like, object=obj, request=request)

    if request.is_ajax():
        html_ctx = widget_context(request.user, obj)
        template = "pinax/likes/_widget.html"
        if request.GET.get("t") == "b":
            template = "pinax/likes/_widget_brief.html"
        data = {
            "html": render_to_string(
                template,
                html_ctx,
                context_instance=RequestContext(request)
            ),
            "likes_count": html_ctx["like_count"],
            "liked": html_ctx["liked"],
        }
        return HttpResponse(json.dumps(data), content_type="application/json")

    return redirect(request.META.get("HTTP_REFERER", "/"))
