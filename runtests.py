#!/usr/bin/env python
import os
import sys

import django

from django.conf import settings


DEFAULT_SETTINGS = dict(
    INSTALLED_APPS=[
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.sites",
        "pinax.likes",
        "pinax.likes.tests"
    ],
    MIDDLEWARE_CLASSES=[],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    },
    SITE_ID=1,
    ROOT_URLCONF="pinax.likes.tests.urls",
    SECRET_KEY="notasecret",
    PINAX_LIKES_LIKABLE_MODELS={
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
    AUTHENTICATION_BACKENDS=[
        "pinax.likes.auth_backends.CanLikeBackend"
    ],
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "APP_DIRS": True,
            "OPTIONS": {
                "debug": True,
                "context_processors": [
                    "django.contrib.auth.context_processors.auth",
                ]
            }
        },
    ]
)


def runtests(*test_args):
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)

    django.setup()

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    try:
        from django.test.runner import DiscoverRunner
        runner_class = DiscoverRunner
        test_args = ["pinax.likes.tests"]
    except ImportError:
        from django.test.simple import DjangoTestSuiteRunner
        runner_class = DjangoTestSuiteRunner
        test_args = ["tests"]

    failures = runner_class(verbosity=1, interactive=True, failfast=False).run_tests(test_args)
    sys.exit(failures)


if __name__ == "__main__":
    runtests(*sys.argv[1:])
