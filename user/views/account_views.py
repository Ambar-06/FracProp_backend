from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from user.serializers.account_serializers import BankAccountDetailSerializer
from user.services.account_services import AccountServices


class AccountViews(BaseAPIView):
    def __init__(self):
        self.service = AccountServices()

    @auth_guard()
    @validate_request()
    def get(self, request, data, *args):
        pass

    @auth_guard()
    @validate_request(BankAccountDetailSerializer)
    def post(self, request, data, *args):
        service_data = self.service.post_service(request, data)
        resp, code = self.get_response_or_error(service_data)
        return self.success(resp, code)
