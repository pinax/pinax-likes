from django.conf import settings
from django.db.models.base import ModelBase


LIKABLE_MODELS = getattr(settings, "PHILEO_LIKABLE_MODELS", [])


def _allowed(model):
    if isinstance(model, ModelBase):
        app_model = "%s.%s" % (model._meta.app_label, model._meta.object_name)
    elif isinstance(model, str):
        app_model = model
    else:
        app_model = str(model)
    
    return app_model in LIKABLE_MODELS

