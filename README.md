![](http://pinaxproject.com/pinax-design/patches/pinax-likes.svg)

# Pinax Likes

[![](https://img.shields.io/pypi/v/pinax-likes.svg)](https://pypi.python.org/pypi/pinax-likes/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://pypi.python.org/pypi/pinax-likes/)

[![CircleCi](https://img.shields.io/circleci/project/github/pinax/pinax-likes.svg)](https://circleci.com/gh/pinax/pinax-likes)
[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-likes.svg)](https://codecov.io/gh/pinax/pinax-likes)
[![](https://img.shields.io/github/contributors/pinax/pinax-likes.svg)](https://github.com/pinax/pinax-likes/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-likes.svg)](https://github.com/pinax/pinax-likes/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-likes.svg)](https://github.com/pinax/pinax-likes/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)


## pinax-likes

`pinax-likes` is a liking app for Django, allowing users to "like" and "unlike"
any model instance in your project. Template tags provide the ability to see who
liked an object, what objects a user liked, and more.


## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Settings](#settings)
* [Templates](#templates)
* [Signals](#signals)
* [Filters](#filters)
* [TemplateTags](#template-tags)
* [Change Log](#change-log)
* [About Pinax](#about-pinax)


## Installation

To install pinax-likes:

    pip install pinax-likes

Add `pinax.likes` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        ...
        "pinax.likes",
        ...
    )

Add the models that you want to be likable to `PINAX_LIKES_LIKABLE_MODELS`:

    PINAX_LIKES_LIKABLE_MODELS = {
        "app.Model": {}  # can override default config settings for each model here
    }

Add `pinax.likes.auth_backends.CanLikeBackend` to your
`AUTHENTICATION_BACKENDS` (or use your own custom version checking
against the `pinax.likes.can_like` permission):

    AUTHENTICATION_BACKENDS = [
        ...
        pinax.likes.auth_backends.CanLikeBackend,
        ...
    ]

Lastly add `pinax.likes.urls` to your project urlpatterns:

    urlpatterns = [
        ...
        url(r"^likes/", include("pinax.likes.urls", namespace="pinax_likes")),
        ...
    ]


## Usage

### Settings

Add each model that you want to be likable to the `PINAX_LIKES_LIKABLE_MODELS` setting:

    PINAX_LIKES_LIKABLE_MODELS = {
        "profiles.Profile": {},
        "videos.Video": {},
        "biblion.Post": {},
    }

### Templates

Let's say you have a detail page for a blog post. First load the template tags:

    {% load pinax_likes_tags %}

In the body where you want the liking widget to go, add:

    {% likes_widget request.user post %}

Finally, ensure you have `eldarion-ajax` installed:

#### Eldarion AJAX

The `likes_widget` templatetag above and the "toggle like" view both conform
to an `AJAX` response that [eldarion-ajax](https://github.com/eldarion/eldarion-ajax) understands.
Furthermore, the templates that ship with this project will work
seemlessly with `eldarion-ajax`. Include the `eldarion-ajax.min.js`
Javascript package in your base template:

    {% load staticfiles %}
    <script src="{% static "js/eldarion-ajax.min.js" %}"></script>

and include `eldarion-ajax` in your site JavaScript:

    require('eldarion-ajax');

Using Eldarion AJAX is optional. You can roll your own JavaScript handling as
the view also returns data in addition to rendered HTML. Furthermore, if
you don't want `ajax` at all the view will handle a regular `POST` and
perform a redirect.


## Signals

Both of these signals are sent from the `Like` model in the view that
processes the toggling of likes and unlikes.

### pinax.likes.signals.object_liked

This signal is sent immediately after the object is liked and provides
the single `kwarg` of `like` which is the created `Like` instance.

### pinax.likes.signals.object_unliked

This signal is sent immediately after the object is unliked and provides
the single `kwarg` of `object` which is the object that was just unliked.


## Filters

#### likes_count

Returns the number of likes for a given object:


    {{ obj|likes_count }}

## Template Tags

### who_likes

An assignment tag that fetches a list of likes for a given object:

    {% who_likes car as car_likes %}

    {% for like in car_likes %}
        <div class="like">{{ like.sender.get_full_name }} likes {{ car }}</div>
    {% endfor %}

### likes

The `likes` tag will fetch into a context variable a list of objects
that the given user likes. This tag has two forms:

1. Obtain `likes` of every model listed in `settings.PINAX_LIKES_LIKABLE_MODELS`:

        {% likes user as objs %}


2. Obtain `likes` for specific models:

        {% likes user "app.Model" as objs %}

#### Example:

    {% likes request.user "app.Model" as objs %}
    {% for obj in objs %}
        <div>{{ obj }}</div>
    {% endfor %}

### render_like

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

### likes_widget

This renders a fragment of HTML the user clicks on
to unlike or like objects. It only has two required parameters,
the user and the object:

    {% likes_widget user object %}

It renders `pinax/likes/_widget.html`.
A second form for this templatetag specifies the template to be rendered:

    {% likes_widget request.user post "pinax/likes/_widget_brief.html" %}

### liked

This template tag decorates an iterable of objects with a
`liked` boolean indicating whether or not the specified
user likes each object in the iterable:

    {% liked objects by request.user as varname %}
    {% for obj in varname %
        <div>{% if obj.liked %}* {% endif %}{{ obj.title }}</div>
    {% endfor %}
    
    
## ChangeLog

### 2.2.0

* Add Django 2.0 compatibility testing
* Drop Django 1.9 and Python 3.3 support
* Move documentation into README
* Convert CI and coverage to CircleCi and CodeCov
* Add PyPi-compatible long description

### 2.1.0

- adds context and request to the `likes_widget` template tag

### 2.0.4

- Improve documentation

### 2.0.1

- Converted documentation to Markdown format

### 2.0.0

- Converted to Django class-based generic views.
- Added URL namespace."pinax_likes"
- Added tests.
- Dropped support for Django 1.7
- Added `compat.py` in order to remove django-user-accounts dependency.

### 1.2

- `like_text_off` and `css_class_off` are passed into widget even if
  `can_like` is False.
- `PINAX_LIKES_LIKABLE_MODELS` entries now take an optional extra
  value `allowed` whose value should be a callable taking `user` and
  `obj` and returning `True` or `False` depending on whether the user is
  allowed to like that particular object

### 1.1.1

-   Fixed regression causing error when widget displayed while unauth'd

### 1.1

-   Fixed `urls.py` deprecation warnings
-   Fixed unicode string
-   Added support for custom User models
-   Documentation updates

### 1.0

-   Added an `admin.py`

### 0.6

-   Added a `likes\_widget\_brief` to display a brief widget template
    (`likes/\_widget\_brief.html`)

### 0.5

-   Added a `who\_likes` template tag that returns a list of `Like` objects
    for given object

### 0.4.1

-   Made the link in the default widget template a bootstrap button

### 0.4

-   Fixed `isinstance` check to check `models.Model` instead of
    `models.base.ModelBase`
-   Added permission checking
-   Added rendering of HTML in the ajax response to liking
-   Got rid of all the `js/css` cruft; up to site owner now but ships with
    bootstrap/bootstrap-ajax enabled templates
-   Updated use of `datetime.datetime.now` to `timezone.now`

#### Backward Incompatibilities

-   Added an `auth\_backend` to check permissions, you can just add the
    `likes.auth\_backends.PermCheckBackend` and do nothing else, or you
    can implement your own backend checking the `likes.can\_like`
    permission against the object and user according to your own
    business logic.
-   No more `likes_css`, `likes_js`, or `likes_widget_js` tags.
-   `PINAX_LIKES_LIKABLE_MODELS` has changed from a `list` to a `dict`
-   `likes_widget` optional parameters have been removed and instead put
    into per model settings

### 0.3

-   Renamed `likes\_css` and `likes\_widget` to `likes\_css` and `likes\_widget`
-   Turned the JavaScript code in to a jQuery plugin, removed most of
    the initialization code from the individual widget templates to a
    external JavaScript file, and added a `{% likes\_js %}` tag to load
    this plugin.
-   Each like button gets a unique ID, so multiple like buttons can
    appear on a single page
-   The like form works without JavaScript.
-   Likable models need to be added to `PINAX\_LIKES\_LIKABLE\_MODELS`
    setting. This prevents users from liking anything and everything,
    which could potentially lead to security problems (eg. liking
    entries in permission tables, and thus seeing their content; liking
    administrative users and thus getting their username).
-   Added request objects to both `object\_liked` and `object\_unliked`
    signals.

#### Backward Incompatibilities

-   Pretty much all the template tags have been renamed and work
    slightly differently

### 0.2

-   Made it easier to get rolling with a like widget using default
    markup and JavaScript
-   Added returning the like counts for an object when it is liked or
    unliked so that the widget (either your own or using the one that
    ships with likes) can update via `AJAX`

#### Backward Incompatibilities

-   Removed `likes\_ajax` and `likes\_form` template tags so if you were
    using them and had written custom overrides in `\_ajax.js` and
    `\_form.html` you'll need to plan your upgrade accordingly.
-   Changed the url pattern, `likes\_like\_toggle`, for likes to not
    require the `user pk`, instead, the view handling the `POST` to this
    url, uses `request.user`.
-   Changed the ajax returned by the `like\_toggle` view so that it now
    just returns a single element: `{"likes\_count": \<some-number\>}`

### 0.1

-   Initial release


## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.

The Pinax documentation is available at http://pinaxproject.com/pinax/. If you would like to help us improve our documentation or write more documentation, please join our Pinax Project Slack team and let us know!

For updates and news regarding the Pinax Project, please follow us on Twitter at @pinaxproject and check out our blog http://blog.pinaxproject.com.

