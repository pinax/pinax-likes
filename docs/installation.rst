.. _installation:

Requirements
============

The view to handle the like toggling conforms to an ajax response that
bootstrap-ajax_ understands. Furthermore, the templates that ship with
this project will work seemlessly with bootstrap-ajax. All you have to
do is include the bootstrap-ajax in your base template somewhere like:

    {% load staticfiles %}
    <script src="{% static "js/bootstrap-ajax.js" %}"></script>

This of course is optional. You can roll your own javascript handling
as the view also returns data in addition to rendered HTML. Furthermore,
if you don't want ajax at all the view will handle a regular POST and
perform a redirect.


Installation
============

* To install phileo::

    pip install phileo

* Add ``'phileo'`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        # other apps
        "phileo",
    )

* Add the models that you want to be likeable to ``PHILEO_LIKABLE_MODELS``:

    PHILEO_LIKABLE_MODELS = {
        "app.Model": {}  # can override default config settings for each model here
    }

* Add ``'phileo.auth_backends.CanLikeBackend'`` to your ``AUTHENTICATION_BACKENDS``
  (or use your own custom version checking against the ``phileo.can_like`` permission):

    AUTHENTICATION_BACKENDS = [
      ...
      "phileo.auth_backends.CanLikeBackend",
      ...
    ]

* Lastly you will want to add `phileo.urls` to your urls definition::

    ...
    url(r"^likes/", include("phileo.urls")),
    ...

:: _bootstrap-ajax: https://github.com/eldarion/bootstrap-ajax
