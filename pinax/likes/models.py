from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone


class Like(models.Model):

    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name="liking", on_delete=models.CASCADE)

    receiver_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    receiver_object_id = models.BigIntegerField()
    receiver = GenericForeignKey(
        ct_field="receiver_content_type",
        fk_field="receiver_object_id"
    )

    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = (
            ("sender", "receiver_content_type", "receiver_object_id"),
        )

    def __str__(self):
        return f"{self.sender} likes {self.receiver}"

    @classmethod
    def like(cls, sender, content_type, object_id):
        obj, liked = cls.objects.get_or_create(
            sender=sender,
            receiver_content_type=content_type,
            receiver_object_id=object_id
        )
        if not liked:
            obj.delete()
        return obj, liked
