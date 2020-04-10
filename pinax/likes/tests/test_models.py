from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from ..models import Like


class LikeTestCase(TestCase):

    def setUp(self):
        self.content_type = ContentType.objects.get(model="user")

    def test_unicode(self):
        u1 = User.objects.create(username="patrick")
        u2 = User.objects.create(username="james")
        like = Like(
            sender=u1,
            receiver_content_type=self.content_type,
            receiver_object_id=u2.pk
        )
        self.assertEquals(str(like), "patrick likes james")

    def test_like(self):
        u1 = User.objects.create(username="patrick")
        u2 = User.objects.create(username="james")
        like, liked = Like.like(u1, self.content_type, u2.pk)
        self.assertTrue(liked)
        self.assertEquals(str(like), "patrick likes james")

    def test_unlike(self):
        u1 = User.objects.create(username="patrick")
        u2 = User.objects.create(username="james")
        like, liked = Like.like(u1, self.content_type, u2.pk)
        like, liked = Like.like(u1, self.content_type, u2.pk)
        self.assertFalse(liked)

    def test_big_integer_receiver_object_id(self):
        u1 = User.objects.create(username="patrick")
        # With Django's BigIntegerField, values from
        # -9223372036854775808 to 9223372036854775807
        # are safe in all databases supported by Django
        # https://docs.djangoproject.com/en/3.0/ref/models/fields/#bigintegerfield
        like, liked = Like.like(u1, self.content_type, 9223372036854775807)
        self.assertTrue(liked)
