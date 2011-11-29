.. _templatetags:

Filters
=======

likes_count
-----------

This simple returns the count of likes for a given object::

    {{ obj|likes_count }}


Template Tags
=============

likes_css
---------

This renders some css style sheets that will style the widget.::

    {% likes_css %}

It renders "phileo/_css.html" and can be overridden as desired.

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

The `render_like` tag looks in the following place for the template to
render. Any of them can be overwritten as needed, allowing you to
customise the rendering of the like on a per model and per application
basis:

* phileo/app_name/model.html
* phileo/app_name/like.html
* phileo/_like.html

phileo_js
---------

This renders some script tags that are needed to make the widget work.::

    {% phileo_js %}

It renders "phileo/_js.html" and can be overridden as desired.


phileo_widget
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
