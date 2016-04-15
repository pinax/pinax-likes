# Filters

## likes_count

Returns the number of likes for a given object:


    {{ obj|likes_count }}

# Template Tags

## who_likes

An assignment tag that fetches a list of likes for a given object:

    {% who_likes car as car_likes %}

    {% for like in car_likes %}
        <div class="like">{{ like.sender.get_full_name }} likes {{ car }}</div>
    {% endfor %}

## likes

The `likes` tag will fetch into a context variable a list of objects
that the given user likes. This tag has two forms:

1. Obtain `likes` of every model listed in `settings.PINAX_LIKES_LIKABLE_MODELS`:

        {% likes user as objs %}


2. Obtain `likes` for specific models:

        {% likes user "app.Model" as objs %}

### Example:

    {% likes request.user "app.Model" as objs %}
    {% for obj in objs %}
        <div>{{ obj }}</div>
    {% endfor %}

## render_like

This renders a like. It combines well with the `likes` templatetag
for showing a list of likes:

    {% likes user as like_list %}
    <ul>
        {% for like in like_list %}
            <li>{% render_like like %}</li>
        {% endfor %}
    </ul>

The `render_like tag` looks in the following places for the template to
render. Any of them can be overwritten as needed, allowing you to
customize the rendering of the like on a per model and per application
basis:

-   `pinax/likes/app_name/model.html`
-   `pinax/likes/app_name/like.html`
-   `pinax/likes/_like.html`

## likes_widget

This renders a fragment of HTML the user clicks on
to unlike or like objects. It only has two required parameters,
the user and the object:

    {% likes_widget user object %}

It renders `pinax/likes/_widget.html`.
A second form for this templatetag specifies the template to be rendered:

    {% likes_widget request.user post "pinax/likes/_widget_brief.html" %}

## liked

This template tag decorates an iterable of objects with a
`liked` boolean indicating whether or not the specified
user likes each object in the iterable:

    {% liked objects by request.user as varname %}
    {% for obj in varname %
        <div>{% if obj.liked %}* {% endif %}{{ obj.title }}</div>
    {% endfor %}
