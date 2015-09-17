import pkg_resources


__version__ = pkg_resources.get_distribution("pinax-likes").version


default_app_config = "pinax.likes.apps.AppConfig"
