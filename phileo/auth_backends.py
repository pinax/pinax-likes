from django.contrib.auth.backends import ModelBackend

from phileo.utils import _allowed


class CanLikeBackend(ModelBackend):
    supports_object_permissions = True
    supports_anonymous_user = True
    
    def has_perm(self, user, perm, obj=None):
        if perm == "phileo.can_like":
            return _allowed(
                "%s.%s" % (s.__class__.__module__, s.__class__.__name__)
            )
        return super(SitePermissionsBackend, self).has_perm(user, perm)
