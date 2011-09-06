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

* Lastly you will want to add `phileo.urls` to your urls definition::

    ...
    url(r"^likes/", include("phileo.urls")),
    ...
