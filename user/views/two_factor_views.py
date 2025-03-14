from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from user.serializers.two_factor_serializers import TwoFactorFilterSerializer
from user.services.two_factor_services import TwoFactorServices


class TwoFactorView(BaseAPIView):

    def __init__(self):
        self.service = TwoFactorServices()

    @auth_guard()
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.response(response, code)

    @auth_guard()
    @validate_request(TwoFactorFilterSerializer)
    def post(self, request, data, *args):
        service_data = self.service.post_service(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.response(response, code)