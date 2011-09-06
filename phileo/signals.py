import django.dispatch


object_liked = django.dispatch.Signal(providing_args=["like"])
object_unliked = django.dispatch.Signal(providing_args=["object"])
