import json

from django.test import TestCase, RequestFactory

from django.contrib.auth.models import AnonymousUser, User
from django.contrib.contenttypes.models import ContentType

from ..models import Like
from ..views import like_toggle


class LikeToggleTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(username="patrick")
        self.other_users = []
        self.user_content_type = ContentType.objects.get(model="user")
        for other_user in ["james", "brian", "michael", "tom", "yulka"]:
            self.other_users.append(
                User.objects.create(username=other_user)
            )
        Like.objects.create(
            sender=self.user,
            receiver_content_type=self.user_content_type,
            receiver_object_id=self.other_users[0].pk
        )
        self.like_qs = Like.objects.filter(sender=self.user, receiver_content_type=self.user_content_type)

    def test_like_brian(self):
        brian = User.objects.get(username="brian")
        request = self.factory.post("/like/{0}:{1}/".format(self.user_content_type.pk, brian.pk))
        request.user = self.user
        response = like_toggle(request, self.user_content_type.pk, brian.pk)
        self.assertEquals(response.status_code, 302)
        self.assertTrue(self.like_qs.filter(receiver_object_id=brian.pk).exists())

    def test_like_brian_unauthed(self):
        brian = User.objects.get(username="brian")
        request = self.factory.post("/like/{0}:{1}/".format(self.user_content_type.pk, brian.pk))
        request.user = AnonymousUser()
        response = like_toggle(request, self.user_content_type.pk, brian.pk)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, "/accounts/login/?next=/like/3%3A3/")
        self.assertFalse(self.like_qs.filter(receiver_object_id=brian.pk).exists())

    def test_unlike_james(self):
        james = User.objects.get(username="james")
        request = self.factory.post("/like/{0}:{1}/".format(self.user_content_type.pk, james.pk))
        request.user = self.user
        response = like_toggle(request, self.user_content_type.pk, james.pk)
        self.assertEquals(response.status_code, 302)
        self.assertFalse(self.like_qs.filter(receiver_object_id=james.pk).exists())

    def test_unlike_james_ajax(self):
        james = User.objects.get(username="james")
        request = self.factory.post(
            "/like/{0}:{1}/".format(self.user_content_type.pk, james.pk),
            HTTP_X_REQUESTED_WITH="XMLHttpRequest"
        )
        request.user = self.user
        response = like_toggle(request, self.user_content_type.pk, james.pk)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(self.like_qs.filter(receiver_object_id=james.pk).exists())
        data = json.loads(response.content.decode())
        self.assertEquals(data["likes_count"], 0)
        self.assertEquals(data["liked"], False)
        self.assertTrue("html" in data)

    def test_like_michael_ajax(self):
        michael = User.objects.get(username="michael")
        request = self.factory.post(
            "/like/{0}:{1}/".format(self.user_content_type.pk, michael.pk),
            HTTP_X_REQUESTED_WITH="XMLHttpRequest"
        )
        request.user = self.user
        response = like_toggle(request, self.user_content_type.pk, michael.pk)
        self.assertEquals(response.status_code, 200)
        self.assertTrue(self.like_qs.filter(receiver_object_id=michael.pk).exists())
        data = json.loads(response.content.decode())
        self.assertEquals(data["likes_count"], 1)
        self.assertEquals(data["liked"], True)
        self.assertTrue("html" in data)

    def test_multiple_like_michael_ajax(self):
        michael = User.objects.get(username="michael")
        request = self.factory.post(
            "/like/{0}:{1}/".format(self.user_content_type.pk, michael.pk),
            HTTP_X_REQUESTED_WITH="XMLHttpRequest"
        )
        request.user = self.user
        response = like_toggle(request, self.user_content_type.pk, michael.pk)
        request.user = User.objects.get(username="tom")
        response = like_toggle(request, self.user_content_type.pk, michael.pk)
        self.assertEquals(response.status_code, 200)
        self.assertTrue(self.like_qs.filter(receiver_object_id=michael.pk).exists())
        data = json.loads(response.content.decode())
        self.assertEquals(data["likes_count"], 2)
        self.assertEquals(data["liked"], True)
        self.assertTrue("html" in data)
