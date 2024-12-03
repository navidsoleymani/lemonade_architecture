from django.conf import settings

try:
    project_settings = settings.HSG_USER1
except:
    project_settings = {}


def import_class(inp: str):
    import importlib

    module_address, klass_name = inp.rsplit('.', 1)
    module = importlib.import_module(module_address)
    ret = getattr(module, klass_name)
    return ret
