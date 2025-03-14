from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from user.services.dashboard_services import DashboardService


class DashboardView(BaseAPIView):
    def __init__(self):
        self.service = DashboardService()

    @auth_guard()
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.response(response, code=code)
