class Response(object):
    def __init__(self, data=None, status_code=None, messages=None):
        self.data = data
        self.status_code = status_code or 200
        self.messages = messages or []


class Interface:
    pass
