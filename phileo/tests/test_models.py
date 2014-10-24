from django.test import TestCase

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from ..models import Like


class LikeTestCase(TestCase):

    def test_unicode(self):
        u1 = User.objects.create(username="patrick")
        u2 = User.objects.create(username="james")
        like = Like(
            sender=u1,
            receiver_content_type=ContentType.objects.get(model="user"),
            receiver_object_id=u2.pk
        )
        self.assertEquals(str(like), "patrick likes james")
