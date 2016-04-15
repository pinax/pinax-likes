# Signals

Both of these signals are sent from the `Like` model in the view that
processes the toggling of likes and unlikes.

## pinax.likes.signals.object_liked

This signal is sent immediately after the object is liked and provides
the single `kwarg` of `like` which is the created `Like` instance.

## pinax.likes.signals.object_unliked

This signal is sent immediately after the object is unliked and provides
the single `kwarg` of `object` which is the object that was just unliked.
