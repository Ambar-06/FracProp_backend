from common.boilerplate.api.base_api import BaseAPIView, BaseModelViewSet
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from property.serializers.property_serializers import (
    PropertyFilterSerializer,
)
from property.services.property_services import PropertyServices


class PropertyView(BaseAPIView):
    def __init__(self):
        self.service = PropertyServices()

    @auth_guard()
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        response, status_code = self.get_response_or_error(service_data)
        return self.success(response, status_code)

    @auth_guard(admin=True)
    @validate_request(PropertyFilterSerializer)
    def post(self, request, data, *args):
        service_data = self.service.post_service(request, data)
        response, status_code = self.get_response_or_error(service_data)
        return self.success(response, status_code)
