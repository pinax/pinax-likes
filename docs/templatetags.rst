.. _templatetags:

Template Tags
=============

likes_css
---------

This renders some css style sheets that will style the widget.::

    {% likes_css %}

It renders "phileo/_css.html" and can be overridden as desired.


likes_widget
------------

This renders a fragement of html that will be what the user will click
on to unlike or like objects. It only has two required parameters, which
are the user and the object.

    {% likes_widget user object [like_link_id="likes" like_span_total_class="phileo-count" toggle_class="phileo-liked"] %}


It renders "phileo/_widget.html" and can be overridden as desired.


likes_js
--------

This is a simple inclusion template tag that will render a bit
of javascript for doing the ajax toggling of a user's like for
a given object. The only two required parameters are the first
two which are the user doing the liking and the object that is
the subject of the liking.::

    {% likes_js user object [like_link="#likes" like_span_total="phileo-count" toggle_class="phileo-liked"] %}

It renders "phileo/_script.html" and can be overriden as desired.


liked
-----

The "liked" template tag will decorate a iterable of objects given
a particular user, with a "liked" boolean indicating whether or not
the user likes each object in the iterable::
    
    {% liked objects by request.user as varname %}
    {% for obj in varname %
        <div>{% if obj.liked %}* {% endif %}{{ obj.title }}</div>
    {% endfor %}


likes
-----

The "likes" tag will fetch into a context variable a list of objects
that the given user likes::

    {% likes request.user "app.Model" as objs %}
    {% for obj in objs %}
        <div>{{ obj }}</div>
    {% endfor %}
