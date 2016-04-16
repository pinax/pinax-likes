# Usage

## Settings

Add each model that you want to be likable to the `PINAX_LIKES_LIKABLE_MODELS` setting:

    PINAX_LIKES_LIKABLE_MODELS = {
        "profiles.Profile": {},
        "videos.Video": {},
        "biblion.Post": {},
    }

## Templates

Let's say you have a detail page for a blog post. First load the template tags:

    {% load pinax_likes_tags %}

In the body where you want the liking widget to go, add:

    {% likes_widget request.user post %}

Finally, ensure you have `eldarion-ajax` installed:

### Eldarion AJAX

The `likes_widget` templatetag above and the "toggle like" view both conform
to an `AJAX` response that [eldarion-ajax](https://github.com/eldarion/eldarion-ajax) understands.
Furthermore, the templates that ship with this project will work
seemlessly with `eldarion-ajax`. All you have to do is include the
eldarion-ajax.min.js Javascript package in your base template:

    {% load staticfiles %}
    <script src="{% static "js/eldarion-ajax.min.js" %}"></script>

and include `eldarion-ajax` in your site JavaScript:

    require('eldarion-ajax');

This of course is optional. You can roll your own JavaScript handling as
the view also returns data in addition to rendered HTML. Furthermore, if
you don't want `ajax` at all the view will handle a regular `POST` and
perform a redirect.
