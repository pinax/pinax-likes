.. _usage:

Usage
=====

Phileo consists of template tags that you place within your project
to get different "liking" functionality.

Let's say you have a detail page for a blog post. First you will want
to load the tags::

    {% load phileo_tags %}


Then in the <head> section of your template load the css::

    {% likes_css %}


In the body where you want the liking widget to go, add::

    {% likes_widget request.user post %}


Then at the bottom of your page where include your javascript::

    {% likes_js request.user post %}


That's all you need to do to get the basics working.