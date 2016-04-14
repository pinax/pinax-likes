Usage
=====

In your settings
----------------

You need to add each model that you want to be likable to the
`PINAX\_LIKES\_LIKABLE\_MODELS` setting:

    ```
    PINAX_LIKES_LIKABLE_MODELS = {
        "profiles.Profile": {},
        "videos.Video": {},
        "biblion.Post": {},
    }

    ```

In the templates
----------------

Let's say you have a detail page for a blog post. First you will want to
load the tags:

    ```
    {% load pinax_likes_tags %}

    ```

In the body where you want the liking widget to go, add:

    ```
    {% likes_widget request.user post %}
    
    ```

That's all you need to do to get the basics working.
