.. _installation:

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
