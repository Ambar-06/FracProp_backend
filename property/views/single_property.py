from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from property.serializers.property_investment_serializers import (
    PropertyInvestmentSerializer,
)
from property.serializers.single_property_serializers import (
    SinglePropertyFilterSerializer,
)
from property.services.property_investment_services import PropertyInvestmentServices
from property.services.single_property_services import SinglePropertyServices


class SinglePropertyView(BaseAPIView):
    headers = {}

    def __init__(self):
        self.service = SinglePropertyServices()
        self.investment_service = PropertyInvestmentServices()

    def dispatch(self, request, *args, **kwargs):
        """Redirect POST requests to the `invest` method if the URL ends with 'invest/'."""
        if request.method == "POST" and request.path.endswith("invest/"):
            request = self.initialize_request(request)
            response = self.invest(request, *args, **kwargs)
            return self.finalize_response(request, response, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    @auth_guard()
    @validate_request(SinglePropertyFilterSerializer)
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        response, status_code = self.get_response_or_error(service_data)
        return self.response(response, status_code)

    @auth_guard(staff=True)
    @validate_request(SinglePropertyFilterSerializer)
    def patch(self, request, data, *args, **kwargs):
        service_data = self.service.patch_service(request, data)
        response, status_code = self.get_response_or_error(service_data)
        return self.response(response, status_code)

    @auth_guard(admin=True)
    @validate_request(SinglePropertyFilterSerializer)
    def delete(self, request, data, *args):
        service_data = self.service.delete_service(request, data)
        response, status_code = self.get_response_or_error(service_data)
        return self.response(response, status_code)

    @auth_guard()
    @validate_request(PropertyInvestmentSerializer)
    def invest(self, request, data, *args):
        service_data = self.investment_service.post_service(request, data)
        response, status_code = self.get_response_or_error(service_data)
        return self.response(response, status_code)

    @auth_guard()
    @validate_request(PropertyInvestmentSerializer)
    def approve(self, request, data, *args):
        service_data = self.investment_service.post_service(request, data)
        response, status_code = self.get_response_or_error(service_data)
        return self.response(response, status_code)
