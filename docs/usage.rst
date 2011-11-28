.. _usage:

Usage
=====

In your models
--------------

You need to register the models that will be 'likeable' with phileo, before
you use phileo in templates::

    # in models.py
    from phileo.handlers import library as phileo_library

    # Define your models ...

    # Register a single model
    phileo_library.register(Post)

    # Register a bunch of models at once
    phileo_library.register([Page, Entry, Comment, Photo])

In the views
------------

Let's say you have a detail page for a blog post. First you will want
to load the tags::

    {% load phileo_tags %}


In the body where you want the liking widget to go, add::

    {% likes_widget request.user post %}


Then at the bottom of your page where include your javascript::

    {% likes_js request.user post %}


That's all you need to do to get the basics working.
