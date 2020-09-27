import importlib

def dynamic_import(module_name, attr_name=None):
    module = importlib.import_module(module_name)
    if not attr_name:
        return module
    attr = getattr(module, attr_name)
    return attr