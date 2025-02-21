from common.boilerplate.services.base_service import BaseService
from investment.helpers.investment_helper import InvestmentHelper
from user.models.user import User


class InvestmentServices(BaseService):
    def __init__(self):
        self.helper = InvestmentHelper()

    def post_service(self, request, data):
        pass

    def get_service(self, request, data):
        user = User.objects.filter(uuid=request.user.get("uuid")).first()
        if not user:
            return self.bad_request("User not found")
        user_investment_data = self.helper.get_investment_data(user)
        return self.ok(user_investment_data)
