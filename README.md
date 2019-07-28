![](http://pinaxproject.com/pinax-design/patches/pinax-likes.svg)

# Pinax Likes

[![](https://img.shields.io/pypi/v/pinax-likes.svg)](https://pypi.python.org/pypi/pinax-likes/)

[![CircleCi](https://img.shields.io/circleci/project/github/pinax/pinax-likes.svg)](https://circleci.com/gh/pinax/pinax-likes)
[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-likes.svg)](https://codecov.io/gh/pinax/pinax-likes)
[![](https://img.shields.io/github/contributors/pinax/pinax-likes.svg)](https://github.com/pinax/pinax-likes/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-likes.svg)](https://github.com/pinax/pinax-likes/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-likes.svg)](https://github.com/pinax/pinax-likes/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Table of Contents

* [About Pinax](#about-pinax)
* [Overview](#overview)
  * [Supported Django and Python versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Signals](#signals)
  * [Filters](#filters)
  * [Template Tags](#template-tags)
  * [Settings](#settings)
  * [Templates](#templates)
* [Change Log](#change-log)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)
  
  
## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable
Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.


## pinax-likes

`pinax-likes` is a liking app for Django, allowing users to "like" and "unlike"
any model instance in your project. Template tags provide the ability to see who
liked an object, what objects a user liked, and more.

`pinax-likes` is not a karma system. It does not have down-voting.


### Overview

#### Supported Django and Python versions

Django \ Python | 2.7 | 3.4 | 3.5 | 3.6
--------------- | --- | --- | --- | ---
1.11 |  *  |  *  |  *  |  *  
2.0  |     |  *  |  *  |  *


## Documentation

### Installation

To install pinax-likes:

```shell
    $ pip install pinax-likes
```

Add `pinax.likes` to your `INSTALLED_APPS` setting:

```python
    INSTALLED_APPS = [
        # other apps
        "pinax.likes",
    ]
```

Add the models that you want to be likable to `PINAX_LIKES_LIKABLE_MODELS` in your settings file:

```python
    PINAX_LIKES_LIKABLE_MODELS = {
        "app.Model": {}  # override default config settings for each model in this dict
    }
```

Add `pinax.likes.auth_backends.CanLikeBackend` to your
`AUTHENTICATION_BACKENDS` (or use your own custom version checking
against the `pinax.likes.can_like` permission):

```python
    AUTHENTICATION_BACKENDS = [
        # other backends
        pinax.likes.auth_backends.CanLikeBackend,
    ]
```

Add `pinax.likes.urls` to your project urlpatterns:

```python
    urlpatterns = [
        # other urls
        url(r"^likes/", include("pinax.likes.urls", namespace="pinax_likes")),
    ]
```

### Usage

Add each model that you want to be likable to the `PINAX_LIKES_LIKABLE_MODELS` setting:

```python
    PINAX_LIKES_LIKABLE_MODELS = {
        "profiles.Profile": {},
        "videos.Video": {},
        "biblion.Post": {},
    }
```

Display "like" widgets in your Django templates.
Suppose you have a detail page for a blog post. First load the template tags:

```django
    {% load pinax_likes_tags %}
```

In the body where you want the liking widget to go, add:

```django
    {% likes_widget request.user post %}
```

Finally, ensure you have `eldarion-ajax` installed:

#### Eldarion AJAX

The `likes_widget` templatetag above and the "toggle like" view both conform
to an `AJAX` response that [eldarion-ajax](https://github.com/eldarion/eldarion-ajax) understands.
Furthermore, the templates that ship with this project will work
seemlessly with `eldarion-ajax`. Include the `eldarion-ajax.min.js`
Javascript package in your base template:

```django
    {% load staticfiles %}
    <script src="{% static "js/eldarion-ajax.min.js" %}"></script>
```

and include `eldarion-ajax` in your site JavaScript:

```javascript
    require('eldarion-ajax');
```

Using Eldarion AJAX is optional. You can roll your own JavaScript handling as
the view also returns data in addition to rendered HTML. Furthermore, if
you don't want `ajax` at all the view will handle a regular `POST` and
perform a redirect.

### Signals

Both of these signals are sent from the `Like` model in the view that
processes the toggling of likes and unlikes.

#### pinax.likes.signals.object_liked

This signal is sent immediately after the object is liked and provides
the single `kwarg` of `like` which is the created `Like` instance.

#### pinax.likes.signals.object_unliked

This signal is sent immediately after the object is unliked and provides
the single `kwarg` of `object` which is the object that was just unliked.

### Filters

##### likes_count

Returns the number of likes for a given object:

```django
    {{ obj|likes_count }}
```

### Template Tags

#### who_likes

An assignment tag that fetches a list of likes for a given object:

```django
    {% who_likes car as car_likes %}

    {% for like in car_likes %}
        <div class="like">{{ like.sender.get_full_name }} likes {{ car }}</div>
    {% endfor %}
```

#### likes

The `likes` tag will fetch into a context variable a list of objects
that the given user likes. This tag has two forms:

1. Obtain `likes` of every model listed in `settings.PINAX_LIKES_LIKABLE_MODELS`:

```django
    {% likes user as objs %}
```

2. Obtain `likes` for specific models:

```django
    {% likes user "app.Model" as objs %}
```

##### Example:

```django
    {% likes request.user "app.Model" as objs %}
    {% for obj in objs %}
        <div>{{ obj }}</div>
    {% endfor %}
```

#### render_like

This renders a like. It combines well with the `likes` templatetag
for showing a list of likes:

```django
    {% likes user as like_list %}
    <ul>
        {% for like in like_list %}
            <li>{% render_like like %}</li>
        {% endfor %}
    </ul>
```

The `render_like tag` looks in the following places for the template to
render. Any of them can be overwritten as needed, allowing you to
customize the rendering of the like on a per model and per application
basis:

-   `pinax/likes/app_name/model.html`
-   `pinax/likes/app_name/like.html`
-   `pinax/likes/_like.html`

#### likes_widget

This renders a fragment of HTML the user clicks on
to unlike or like objects. It only has two required parameters,
the user and the object:

```django
    {% likes_widget user object %}
```

It renders `pinax/likes/_widget.html`.
A second form for this templatetag specifies the template to be rendered:

```django
    {% likes_widget request.user post "pinax/likes/_widget_brief.html" %}
```

#### liked

This template tag decorates an iterable of objects with a
`liked` boolean indicating whether or not the specified
user likes each object in the iterable:

```django
    {% liked objects by request.user as varname %}
    {% for obj in varname %
        <div>{% if obj.liked %}* {% endif %}{{ obj.title }}</div>
    {% endfor %}
```    

### Settings

#### PINAX_LIKES_LIKABLE_MODELS

A dictionary keyed by "<appname.model>". Each model value is a dictionary containing context keys and values.

Context value keys are CSS element names used in template rendering for each model:

##### `"count_text_singular"`

##### `"count_text_plural"`

##### `"css_class_off"`

##### `"css_class_on"`

##### `"like_text_off"`

##### `"like_text_on"`

Here is an example from the test settings used on this project found in runtests.py.

```python
    PINAX_LIKES_LIKABLE_MODELS = {
        "auth.User": {
            "like_text_on": "unlike",
            "css_class_on": "fa-heart",
            "like_text_off": "like",
            "css_class_off": "fa-heart-o",
            "allowed": lambda user, obj: True
        },
        "tests.Demo": {
            "like_text_on": "unlike",
            "css_class_on": "fa-heart",
            "like_text_off": "like",
            "css_class_off": "fa-heart-o"
        }
    },
```

### Templates

`pinax-likes` uses minimal template snippets rendered with template tags.

Default templates are provided by the `pinax-templates` app in the
[likes](https://github.com/pinax/pinax-templates/tree/master/pinax/templates/templates/pinax/likes)
section of that project.

Reference pinax-templates
[installation instructions](https://github.com/pinax/pinax-templates/blob/master/README.md#installation)
to include these templates in your project.

View live `pinax-templates` examples and source at [Pinax Templates](https://templates.pinaxproject.com/likes/fragments/)!

#### Customizing Templates

Override the default `pinax-templates` templates by copying them into your project
subdirectory `pinax/likes/` on the template path and modifying as needed.

For example if your project doesn't use Bootstrap, copy the desired templates
then remove Bootstrap and Font Awesome class names from your copies.
Remove class references like `class="btn btn-success"` and `class="icon icon-pencil"` as well as
`bootstrap` from the `{% load i18n bootstrap %}` statement.
Since `bootstrap` template tags and filters are no longer loaded, you'll also need to update
`{{ form|bootstrap }}` to `{{ form }}` since the "bootstrap" filter is no longer available.

#### `_like.html`

#### `_widget.html`

#### `_widget_brief.html`

    
## Change Log

## 3.0.1

* Add django>=1.11 to requirements
* Improve documentation markup
* Remove doc build support
* Update CI config
* Replace pinax-theme-bootstrap with pinax-templates for testing

## 3.0.0

* Drop Django 1.8 and 1.10 support
* Improve documentation

### 2.2.1

* Correct LONG_DESCRIPTION app title

### 2.2.0

* Add Django 2.0 compatibility testing
* Drop Django 1.9 and Python 3.3 support
* Move documentation into README
* Convert CI and coverage to CircleCi and CodeCov
* Add PyPi-compatible long description

### 2.1.0

* adds context and request to the `likes_widget` template tag

### 2.0.4

* Improve documentation

### 2.0.1

* Converted documentation to Markdown format

### 2.0.0

* Converted to Django class-based generic views.
* Added URL namespace."pinax_likes"
* Added tests.
* Dropped support for Django 1.7
* Added `compat.py` in order to remove django-user-accounts dependency.

### 1.2

* `like_text_off` and `css_class_off` are passed into widget even if
  `can_like` is False.
* `PINAX_LIKES_LIKABLE_MODELS` entries now take an optional extra
  value `allowed` whose value should be a callable taking `user` and
  `obj` and returning `True` or `False` depending on whether the user is
  allowed to like that particular object

### 1.1.1

* Fixed regression causing error when widget displayed while unauth'd

### 1.1

* Fixed `urls.py` deprecation warnings
* Fixed unicode string
* Added support for custom User models
* Documentation updates

### 1.0

* Added an `admin.py`

### 0.6

* Added a `likes\_widget\_brief` to display a brief widget template
    (`likes/\_widget\_brief.html`)

### 0.5

* Added a `who\_likes` template tag that returns a list of `Like` objects
    for given object

### 0.4.1

* Made the link in the default widget template a bootstrap button

### 0.4

* Fixed `isinstance` check to check `models.Model` instead of
    `models.base.ModelBase`
* Added permission checking
* Added rendering of HTML in the ajax response to liking
* Got rid of all the `js/css` cruft; up to site owner now but ships with
    bootstrap/bootstrap-ajax enabled templates
* Updated use of `datetime.datetime.now` to `timezone.now`

#### Backward Incompatibilities

* Added an `auth\_backend` to check permissions, you can just add the
    `likes.auth\_backends.PermCheckBackend` and do nothing else, or you
    can implement your own backend checking the `likes.can\_like`
    permission against the object and user according to your own
    business logic.
* No more `likes_css`, `likes_js`, or `likes_widget_js` tags.
* `PINAX_LIKES_LIKABLE_MODELS` has changed from a `list` to a `dict`
* `likes_widget` optional parameters have been removed and instead put
    into per model settings

### 0.3

* Renamed `likes\_css` and `likes\_widget` to `likes\_css` and `likes\_widget`
* Turned the JavaScript code in to a jQuery plugin, removed most of
    the initialization code from the individual widget templates to a
    external JavaScript file, and added a `{% likes\_js %}` tag to load
    this plugin.
* Each like button gets a unique ID, so multiple like buttons can
    appear on a single page
* The like form works without JavaScript.
* Likable models need to be added to `PINAX\_LIKES\_LIKABLE\_MODELS`
    setting. This prevents users from liking anything and everything,
    which could potentially lead to security problems (eg. liking
    entries in permission tables, and thus seeing their content; liking
    administrative users and thus getting their username).
* Added request objects to both `object\_liked` and `object\_unliked`
    signals.

#### Backward Incompatibilities

* Pretty much all the template tags have been renamed and work
    slightly differently

### 0.2

* Made it easier to get rolling with a like widget using default
    markup and JavaScript
* Added returning the like counts for an object when it is liked or
    unliked so that the widget (either your own or using the one that
    ships with likes) can update via `AJAX`

#### Backward Incompatibilities

* Removed `likes\_ajax` and `likes\_form` template tags so if you were
    using them and had written custom overrides in `\_ajax.js` and
    `\_form.html` you'll need to plan your upgrade accordingly.
* Changed the url pattern, `likes\_like\_toggle`, for likes to not
    require the `user pk`, instead, the view handling the `POST` to this
    url, uses `request.user`.
* Changed the ajax returned by the `like\_toggle` view so that it now
    just returns a single element: `{"likes\_count": \<some-number\>}`

### 0.1

* Initial release


## Contribute

For an overview on how contributing to Pinax works read this [blog post](http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/)
and watch the included video, or read our [How to Contribute](http://pinaxproject.com/pinax/how_to_contribute/) section.
For concrete contribution ideas, please see our
[Ways to Contribute/What We Need Help With](http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you join our [Pinax Slack team](http://slack.pinaxproject.com)
and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course
also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our blog post on [Open Source and Self-Care](http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).


## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project
has a [code of conduct](http://pinaxproject.com/pinax/code_of_conduct/).
We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject)
and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-2019 James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).
