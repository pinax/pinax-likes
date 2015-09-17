from django.conf import settings  # noqa
from django.core.exceptions import ImproperlyConfigured

try:
    from importlib import import_module
except ImportError:
    from django.utils.importlib import import_module

from appconf import AppConf
from collections import defaultdict


def load_path_attr(path):
    i = path.rfind(".")
    module, attr = path[:i], path[i + 1:]
    try:
        mod = import_module(module)
    except ImportError as e:
        raise ImproperlyConfigured("Error importing {0}: '{1}'".format(module, e))
    try:
        attr = getattr(mod, attr)
    except AttributeError:
        raise ImproperlyConfigured("Module '{0}' does not define a '{1}'".format(module, attr))
    return attr


class LikeAppConf(AppConf):

    DEFAULT_LIKE_CONFIG = {
        "css_class_on": "icon-heart",
        "css_class_off": "icon-heart-empty",
        "like_text_on": "Unlike",
        "like_text_off": "Like",
        "count_text_singular": "like",
        "count_text_plural": "likes",
    }

    LIKABLE_MODELS = getattr(settings, "PINAX_LIKES_LIKABLE_MODELS", defaultdict(dict))

    for model in LIKABLE_MODELS:
        custom_data = LIKABLE_MODELS[model].copy()
        default_data = DEFAULT_LIKE_CONFIG.copy()
        LIKABLE_MODELS[model] = default_data
        LIKABLE_MODELS[model].update(custom_data)
