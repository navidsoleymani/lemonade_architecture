def request_updater(request, **kwargs):
    if hasattr(request, 'data') and request.data:
        request.data._mutable = True
        for k, v in kwargs.items():
            request.data[k] = v
        request.data._mutable = False
    return request
