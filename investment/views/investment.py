from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from investment.services.investment_services import InvestmentServices


class InvestmentView(BaseAPIView):
    def __init__(self):
        self.service = InvestmentServices()

    @auth_guard()
    # @validate_request(InvestmentFilterSerializer)
    def post(self, request, data, *args):
        data = request.data
        response = self.service.post_service(request, data)
        response, code = self.get_response_or_error(response)
        return self.success(response, code=code)

    @auth_guard()
    def get(self, request, data, *args):
        response = self.service.get_service(request, data)
        response, code = self.get_response_or_error(response)
        return self.success(response, code=code)
