import datetime

from django.db import models

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Like(models.Model):
    
    sender = models.ForeignKey(User, related_name="liking")
    
    receiver_content_type = models.ForeignKey(ContentType)
    receiver_object_id = models.PositiveIntegerField()
    receiver = generic.GenericForeignKey(
        ct_field="receiver_content_type",
        fk_field="receiver_object_id"
    )
    
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        unique_together = (
            ("sender", "receiver_content_type", "receiver_object_id"),
        )
    
    def __unicode__(self):
        return "%s likes %s" % (self.sender, self.receiver)
