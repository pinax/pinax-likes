.. _changelog:

ChangeLog
=========

0.6
---

- Added a `phileo_widget_brief` to display a brief widget template (`phileo/_widget_brief.html`)


0.5
---

- Added a `who_likes` template tag that returns a list of `Like` objects for given object

0.4.1
-----

- Made the link in the default widget template a bootstrap button

0.4
---

- Fixed isinstance check to check ``models.Model`` instead of ``models.base.ModelBase``
- Added permission checking
- Added rendering of HTML in the ajax response to liking
- Got rid of all the js/css cruft; up to site owner now but ships with bootstrap/bootstrap-ajax enabled templates
- Updated use of ``datetime.datetime.now`` to ``timezone.now``

Backward Incompatibilities
^^^^^^^^^^^^^^^^^^^^^^^^^^

- Added an auth_backend to check permissions, you can just add the `phileo.auth_backends.PermCheckBackend`
  and do nothing else, or you can implement you own backend checking the `phileo.can_like`
  permission against the object and user according to your own business logic.
- No more ``phileo_css``, ``phileo_js``, or ``phileo_widget_js`` tags.
- ``PHILEO_LIKABLE_MODELS`` has changed from a ``list`` to a ``dict``
- ``phileo_widget`` optional parameters have been removed and instead put into per model settings


0.3
---

- Renamed `likes_css` and `likes_widget` to `phileo_css` and `phileo_widget`
- Turned the JavaScript code in to a jQuery plugin, removed most of the initialization
  code from the individual widget templates to a external JavaScript file, and added a
  {% phileo_js %} tag to load this plugin.
- Each like button gets a unique ID, so multiple like buttons can appear on a single
  page
- The like form works without JavaScript.
- Likeable models need to be added to `PHILEO_LIKABLE_MODELS` setting. This prevents users
  from liking anything and everything, which could potentially lead to security problems
  (eg. liking entries in permission tables, and thus seeing their content; liking
  administrative users and thus getting their username).
- Added request objects to both `object_liked` and `object_unliked` signals.

Backward Incompatibilities
^^^^^^^^^^^^^^^^^^^^^^^^^^

- pretty much all the template tags have been renamed and work slightly differently


0.2
---

- made it easier to get rolling with a like widget using default markup and javascript
- added returning the like counts for an object when it is liked or unliked so that the
  widget (either your own or using the one that ships with phileo) can update via AJAX

Backward Incompatibilities
^^^^^^^^^^^^^^^^^^^^^^^^^^

- removed `likes_ajax` and `likes_form` template tags so if you were using them and had
  written custom overrides in _ajax.js and _form.html you'll need to plan your upgrade
  accordingly.
- changed the url pattern, `phileo_like_toggle`, for likes to not require the user pk,
  instead, the view handling the POST to this url, uses request.user.
- changed the ajax returned by the `like_toggle` view so that it now just returns a
  single element: {"likes_count": <some-number>}

0.1
---

- initial release
