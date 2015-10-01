.. _templatetags:

Filters
=======

likes_count
-----------

This simple returns the count of likes for a given object::

    {{ obj|likes_count }}


Template Tags
=============

who_likes
---------

An assignment tag that fetches a list of likes for a given object::

    {% who_likes car as car_likes %}

    {% for like in car_likes %}
        <div class="like">{{ like.sender.get_full_name }} likes {{ car }}</div>
    {% endfor %}



render_like
-----------

This renders a like, so that you can provide a list of likes. It
combines well with `likes`.::

    {% likes user as like_list %}
    <ul>
        {% for like in like_list %}
            <li>{% render_like like %}</li>
        {% endfor %}
    </ul>

The `render_like` tag looks in the following places for the template to
render. Any of them can be overwritten as needed, allowing you to
customize the rendering of the like on a per model and per application
basis:

* likes/app_name/model.html
* likes/app_name/like.html
* likes/_like.html


likes_widget
-------------

This renders a fragment of html that will be what the user will click
on to unlike or like objects. It only has two required parameters, which
are the user and the object.::

    {% likes_widget user object %}


It renders "likes/_widget.html" and can be overridden as desired.


likes_widget_brief
-------------------

Same, functionally, as `likes_widget`, except that it renders
"likes/_widget_brief.html" instead.


liked
-----

The "liked" template tag will decorate an iterable of objects given
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
