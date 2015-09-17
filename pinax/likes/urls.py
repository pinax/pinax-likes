from django.conf.urls import url, patterns


urlpatterns = patterns(
    "pinax.likes.views",
    url(r"^like/(?P<content_type_id>\d+):(?P<object_id>\d+)/$", "like_toggle", name="likes_like_toggle")
)
