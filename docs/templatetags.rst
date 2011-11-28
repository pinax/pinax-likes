.. _templatetags:

Filters
=======

likes_count
-----------

This simple returns the count of likes for a given object::

    {{ obj|likes_count }}


Template Tags
=============

phileo_js
---------

This renders some script tags that are needed to make the widget work.::

    {% phileo_js %}

It renders "phileo/_js.html" and can be overridden as desired.


likes_widget
------------

This renders a fragement of html that will be what the user will click
on to unlike or like objects. It only has two required parameters, which
are the user and the object.::

    {% likes_widget user object [widget_id="unique_id" like_type="likes" toggle_class="phileo-liked"] %}


It renders "phileo/_widget.html" and can be overridden as desired.

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
