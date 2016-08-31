from django.test import TestCase

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from .models import Demo

from ..utils import (
    _allowed,
    get_config,
    per_model_perm_check,
)


class UtilsTestCase(TestCase):

    def setUp(self):
        self.content_type = ContentType.objects.get(model="user")

    def test_allowed_model(self):
        self.assertTrue(_allowed(User))

    def test_allowed_str(self):
        self.assertTrue(_allowed("auth.User"))

    def test_allowed_other(self):
        self.assertFalse(_allowed(TestCase))

    def test_get_config_user(self):
        """
        Test like configuration for a User instance.
        """
        config = get_config(User)
        self.assertEquals(config["like_text_on"], "unlike me")
        self.assertEquals(config["css_class_on"], "fa-heart")
        self.assertEquals(config["like_text_off"], "like me")
        self.assertEquals(config["css_class_off"], "fa-heart-o")

        # The following like configuration values are not specified by
        # PINAX_LIKES_LIKABLE_MODELS test setting.
        # Values should come from defaults in pinax/likes/conf.py.
        self.assertEquals(config["count_text_singular"], "like")
        self.assertEquals(config["count_text_plural"], "likes")

    def test_get_config_demo(self):
        """
        Test like configuration for a Demo instance.
        """
        config = get_config(Demo)
        self.assertEquals(config["like_text_on"], "unlike")
        self.assertEquals(config["css_class_on"], "fa-rocketship")
        self.assertEquals(config["like_text_off"], "like")
        self.assertEquals(config["css_class_off"], "fa-rocketship-o")

        # The following like configuration values are not specified by
        # PINAX_LIKES_LIKABLE_MODELS test setting.
        # Values should come from defaults in pinax/likes/conf.py.
        self.assertEquals(config["count_text_singular"], "like")
        self.assertEquals(config["count_text_plural"], "likes")

    def test_per_model_perm_check(self):
        patrick = User.objects.create_user(username="patrick")
        check = per_model_perm_check(patrick, User)
        self.assertTrue(check)

    def test_per_model_perm_check_default(self):
        patrick = User.objects.create_user(username="patrick")
        check = per_model_perm_check(patrick, Demo)
        self.assertTrue(check)
