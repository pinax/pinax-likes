from django.conf.urls.defaults import url, patterns


urlpatterns = patterns("phileo.views",
    url(r"^like/(?P<content_type_id>\d+):(?P<object_id>\d+)/$", "like_toggle", name="phileo_like_toggle")
)
