from django.conf import settings
LIKABLE_MODELS = getattr(settings, "PHILEO_LIKABLE_MODELS", [])

def _allowed(obj):
    model_name = "%s.%s" % (obj._meta.app_label, obj._meta.object_name)
    return model_name in LIKABLE_MODELS

