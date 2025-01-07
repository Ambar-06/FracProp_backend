from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from property.serializers.single_property_serializers import SinglePropertyFilterSerializer
from property.services.single_property_services import SinglePropertyServices


class SinglePropertyView(BaseAPIView):
    def __init__(self):
        self.service = SinglePropertyServices()

    @auth_guard()
    @validate_request(SinglePropertyFilterSerializer)
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        response, status_code = self.get_response_or_error(service_data)
        return self.success(response, status_code)

    @auth_guard(staff=True)
    @validate_request(SinglePropertyFilterSerializer)
    def patch(self, request, data, *args):
        service_data = self.service.patch_service(request, data)
        response, status_code = self.get_response_or_error(service_data)
        return self.success(response, status_code)

    def delete(self, request, data, *args):
        ...