from common.boilerplate.services.base_service import BaseService
from investment.helpers.investment_helper import InvestmentHelper
from investment.models.investment import Investment
from investment.models.transaction import Transaction
from property.helpers.property_valuation_breakout_helper import (
    PropertyValuationBreakoutHelper,
)
from property.models.property import Property
from user.models.user import User


class PropertyInvestmentServices(BaseService):
    def __init__(self):
        self.valuation_helper = PropertyValuationBreakoutHelper()
        self.investment_helper = InvestmentHelper()

    def post_service(self, request, data):
        user = User.objects.filter(uuid=request.user.get("uuid")).first()
        property = Property.objects.filter(uuid=data.get("property_id")).first()
        if not property:
            return self.not_found("Property not found")
        if property.sold_percentage == 100:
            return self.bad_request("Property is already sold out")
        amount = data.get("amount")
        stake_amount, stake_percentage = (
            self.valuation_helper.calculate_amount_proportion_with_valuation(
                amount, property.valuation
            )
        )
        self.investment_helper.perform_post_investment_operations(
            user, property, amount, stake_percentage
        )
        return self.ok("Investment successful")
