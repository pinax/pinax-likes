Requirements
============

The view to handle the like toggling conforms to an `ajax` response that
[eldarion-ajax](https://github.com/eldarion/eldarion-ajax) understands.
Furthermore, the templates that ship with this project will work
seemlessly with `eldarion-ajax`. All you have to do is include the
`eldarion-ajax` in your base template somewhere like:

    ```
    {% load staticfiles %}
    <script src="{% static "js/eldarion-ajax.min.js" %}"></script>

    ````

and include `eldarion-ajax` somewhere in your site JavaScript:

    ```
    require('eldarion-ajax');

    ```

This of course is optional. You can roll your own JavaScript handling as
the view also returns data in addition to rendered HTML. Furthermore, if
you don't want `ajax` at all the view will handle a regular `POST` and
perform a redirect.

Installation
============

-   To install likes:

        ```
        pip install likes

        ```

-   Add `likes` to your `INSTALLED_APPS` setting:

        ```
        INSTALLED_APPS = (
            # other apps
            "likes",
        )

        ```

-   Add the models that you want to be likable to
    `PINAX_LIKES_LIKABLE_MODELS`:

        ```
        PINAX_LIKES_LIKABLE_MODELS = {
            "app.Model": {}  # can override default config settings for each model here
        }

        ```

-   Add `likes.auth_backends.CanLikeBackend` to your
    `AUTHENTICATION_BACKENDS` (or use your own custom version checking
    against the `likes.can_like` permission):

        ```
        AUTHENTICATION_BACKENDS = [

          likes.auth_backends.CanLikeBackend,

        ]

        ```

-   Lastly you will want to add `likes.urls` to your urls definition:

        ```
        url(r"^likes/", include("likes.urls")),
        ```
