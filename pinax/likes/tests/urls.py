from django.conf.urls import include, url


def dummy_view():
    pass

urlpatterns = [
    url(r"^", include("pinax.likes.urls", namespace="pinax_likes")),
    url(r"^dummy_login/$", dummy_view, name="account_login"),
]
