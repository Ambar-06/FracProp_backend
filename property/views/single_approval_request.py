from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from property.models.property_approval_request import PropertyApprovalRequest
from property.serializers.single_approval_request_serializers import (
    SingleApprovalRequestFilterSerializer,
)
from property.services.single_approval_request_services import (
    SingleApprovalRequestServices,
)


class SingleApprovalRequestView(BaseAPIView):
    def __init__(self):
        self.service = SingleApprovalRequestServices()

    @auth_guard(admin=True)
    @validate_request(SingleApprovalRequestFilterSerializer)
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.success(response, code)

    @auth_guard(admin=True)
    @validate_request(SingleApprovalRequestFilterSerializer)
    def patch(self, request, data, *args):
        service_data = self.service.patch_service(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.success(response, code)
