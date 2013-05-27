from tastypie.api import Api

# The Tastypie API handle
v1_api = Api(api_name='v1')


#NOTE: Lifted from django.contrib.admin
def autodiscover():
    """
    Auto-discover INSTALLED_APPS api.py modules and fail silently when not
    present. This forces an import on them to register any API bits they
    may want.
    """
    import copy
    from django.conf import settings
    from django.utils.importlib import import_module
    from django.utils.module_loading import module_has_submodule

    for app in settings.INSTALLED_APPS:
        mod = import_module(app)

        try:
            before_import_registry = copy.copy(v1_api._registry)
            import_module('{0}.api'.format(app))
        except:
            v1_api._registry = before_import_registry
            if module_has_submodule(mod, 'api'):
                raise
