from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from property.services.approval_request_services import ApprovalRequestServices


class ApprovalRequestView(BaseAPIView):
    def __init__(self):
        self.service = ApprovalRequestServices()

    @auth_guard(admin=True)
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.success(response, code)
