from django.conf.urls import url

from . import views


urlpatterns = [
    url(r"^like/(?P<content_type_id>\d+):(?P<object_id>\d+)/$", views.like_toggle, name="likes_like_toggle")
]
