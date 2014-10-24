from django.test import TestCase

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from ..models import Like
from ..templatetags.phileo_tags import ObjectDecorator


class ObjectDecoratorTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="patrick")
        self.other_users = []
        for other_user in ["james", "brian", "michael", "tom", "yulka"]:
            self.other_users.append(
                User.objects.create(username=other_user)
            )
        Like.objects.create(
            sender=self.user,
            receiver_content_type=ContentType.objects.get(model="user"),
            receiver_object_id=self.other_users[0].pk
        )

    def test_object_decorator(self):
        for obj in ObjectDecorator(self.user, self.other_users).objects():
            if obj.username == "james":
                self.assertTrue(obj.liked)
            else:
                self.assertFalse(obj.liked)
