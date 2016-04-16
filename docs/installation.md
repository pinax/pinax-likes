# Installation

To install pinax-likes:

    pip install pinax-likes

Add `pinax.likes` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        ...
        "pinax.likes",
        ...
    )

Add the models that you want to be likable to `PINAX_LIKES_LIKABLE_MODELS`:

    PINAX_LIKES_LIKABLE_MODELS = {
        "app.Model": {}  # can override default config settings for each model here
    }

Add `pinax.likes.auth_backends.CanLikeBackend` to your
`AUTHENTICATION_BACKENDS` (or use your own custom version checking
against the `pinax.likes.can_like` permission):

    AUTHENTICATION_BACKENDS = [
        ...
        pinax.likes.auth_backends.CanLikeBackend,
        ...
    ]

Lastly add `pinax.likes.urls` to your project urlpatterns:

    urlpatterns = [
        ...
        url(r"^likes/", include("pinax.likes.urls", namespace="pinax_likes")),
        ...
    ]

See [Usage](./usage.md) for details about integrating pinax-likes with your project.
