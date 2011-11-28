.. _usage:

Usage
=====

In your settings
----------------

You need to add each model that you want to be likable to the
`PHILEO_LIKABLE_MODELS` setting::

    PHILEO_LIKABLE_MODELS = [
        "profiles.Profile",
        "videos.Video",
        "biblion.Post"
    ]


In the views
------------

Let's say you have a detail page for a blog post. First you will want
to load the tags::

    {% load phileo_tags %}


Then in the <head> section of your template load the css::

    {% phileo_css %}


Load the required JavaScript file, wherever you load your JavaScript libraries::

    {% phileo_js %}


In the body where you want the liking widget to go, add::

    {% phileo_widget request.user post %}


That's all you need to do to get the basics working.
