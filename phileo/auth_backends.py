from django.contrib.auth.backends import ModelBackend

from phileo.utils import _allowed


class CanLikeBackend(ModelBackend):
    supports_object_permissions = True
    supports_anonymous_user = True
    
    def is_allowed(self, obj):
        return _allowed(obj)
    
    def has_perm(self, user, perm, obj=None):
        if perm == "phileo.can_like":
            return self.is_allowed(obj)
        return super(CanLikeBackend, self).has_perm(user, perm)
