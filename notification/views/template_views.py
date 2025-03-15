from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard


class TemplateViews(BaseAPIView):
    def __init__(self):
        self.service = ...

    @auth_guard(admin=True)
    def get(self, request, data, *args):
        pass

    @auth_guard(admin=True)
    def post(self, request, data, *args):
        pass