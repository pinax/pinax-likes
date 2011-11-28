from django.db.models.base import ModelBase

class Registry(object):
    def __init__(self):
        self._registry = []

    def register(self, models):

        if isinstance(models, ModelBase):
            models = [models]

        for model in models:
            self._registry.append(model)

    def is_registered(self, model):
        return not (model in self._registry)

library = Registry()

