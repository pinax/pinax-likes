.. _changelog:

ChangeLog
=========

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
