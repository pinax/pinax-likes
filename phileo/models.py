from django.conf import settings
from django.db import models
from django.utils import timezone

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


# Compatibility with custom user models, while keeping backwards-compatibility with <1.5
AUTH_USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")


class Like(models.Model):

    sender = models.ForeignKey(AUTH_USER_MODEL, related_name="liking")

    receiver_content_type = models.ForeignKey(ContentType)
    receiver_object_id = models.PositiveIntegerField()
    receiver = generic.GenericForeignKey(
        ct_field="receiver_content_type",
        fk_field="receiver_object_id"
    )

    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = (
            ("sender", "receiver_content_type", "receiver_object_id"),
        )

    def __unicode__(self):
        return u"%s likes %s" % (self.sender, self.receiver)
