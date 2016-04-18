# ChangeLog

## 2.0.4

- Improve documentation

## 2.0.1

- Converted documentation to Markdown format

## 2.0.0

- Converted to Django class-based generic views.
- Added URL namespace."pinax_likes"
- Added tests.
- Dropped support for Django 1.7
- Added `compat.py` in order to remove django-user-accounts dependency.

## 1.2

- `like_text_off` and `css_class_off` are passed into widget even if
  `can_like` is False.
- `PINAX_LIKES_LIKABLE_MODELS` entries now take an optional extra
  value `allowed` whose value should be a callable taking `user` and
  `obj` and returning `True` or `False` depending on whether the user is
  allowed to like that particular object

## 1.1.1

-   Fixed regression causing error when widget displayed while unauth'd

## 1.1

-   Fixed `urls.py` deprecation warnings
-   Fixed unicode string
-   Added support for custom User models
-   Documentation updates

## 1.0

-   Added an `admin.py`

## 0.6

-   Added a `likes\_widget\_brief` to display a brief widget template
    (`likes/\_widget\_brief.html`)

## 0.5

-   Added a `who\_likes` template tag that returns a list of `Like` objects
    for given object

## 0.4.1

-   Made the link in the default widget template a bootstrap button

## 0.4

-   Fixed `isinstance` check to check `models.Model` instead of
    `models.base.ModelBase`
-   Added permission checking
-   Added rendering of HTML in the ajax response to liking
-   Got rid of all the `js/css` cruft; up to site owner now but ships with
    bootstrap/bootstrap-ajax enabled templates
-   Updated use of `datetime.datetime.now` to `timezone.now`

### Backward Incompatibilities

-   Added an `auth\_backend` to check permissions, you can just add the
    `likes.auth\_backends.PermCheckBackend` and do nothing else, or you
    can implement your own backend checking the `likes.can\_like`
    permission against the object and user according to your own
    business logic.
-   No more `likes_css`, `likes_js`, or `likes_widget_js` tags.
-   `PINAX_LIKES_LIKABLE_MODELS` has changed from a `list` to a `dict`
-   `likes_widget` optional parameters have been removed and instead put
    into per model settings

## 0.3

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

### Backward Incompatibilities

-   Pretty much all the template tags have been renamed and work
    slightly differently

## 0.2

-   Made it easier to get rolling with a like widget using default
    markup and JavaScript
-   Added returning the like counts for an object when it is liked or
    unliked so that the widget (either your own or using the one that
    ships with likes) can update via `AJAX`

### Backward Incompatibilities

-   Removed `likes\_ajax` and `likes\_form` template tags so if you were
    using them and had written custom overrides in `\_ajax.js` and
    `\_form.html` you'll need to plan your upgrade accordingly.
-   Changed the url pattern, `likes\_like\_toggle`, for likes to not
    require the `user pk`, instead, the view handling the `POST` to this
    url, uses `request.user`.
-   Changed the ajax returned by the `like\_toggle` view so that it now
    just returns a single element: `{"likes\_count": \<some-number\>}`

## 0.1

-   Initial release
