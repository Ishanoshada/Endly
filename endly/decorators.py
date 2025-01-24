# endly/decorators.py
def route(path):
    def decorator(func):
        func.route_path = path
        return func
    return decorator