from common.boilerplate.services.base_service import BaseService
from investment.models.investment_return import InvestmentReturn
from property.models.user_property_amount import UserPropertyAmount
from user.models.user import User
from django.db.models import Sum


class DashboardService(BaseService):
    def __init__(self):
        pass

    def get_service(self, request, data):
        user = User.objects.filter(uuid=request.user.get("uuid")).first()
        if not user:
            return self.not_found("User not found")
        user_properties = user.user_properties.filter(is_deleted=False)
        user_property_amount = UserPropertyAmount.objects.filter(user=user).first()
        user_total_rental_income = (
            InvestmentReturn.objects.filter(user=user, return_type="RENTAL")
            .aggregate(Sum("return_in_amount"))
            .get("return_in_amount__sum", 0)
        )
        dashboard_cards_data = {
            "total_properties": user_properties.count(),
            "total_investment": user_property_amount.total_amount if user_property_amount else 0,
            "total_rental_income": user_total_rental_income if user_total_rental_income else 0,
            "increase_in_valuation": 0,
        }
        return self.ok(dashboard_cards_data)
