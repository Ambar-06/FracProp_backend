from common.boilerplate.services.base_service import BaseService
from investment.models.investment import Investment
from property.models.user_property import UserProperty
from user.models.user import User


class InvestmentServices(BaseService):
    def __init__(self):
        self.model = Investment
        self.user_model = User
        self.user_property_model = UserProperty

    def post_service(self, request, data):
        pass

    def get_service(self, request, data):
        user = self.user_model.objects.filter(uuid=request.user.get("uuid")).first()
        if not user:
            return self.bad_request("User not found")
        if not user.is_admin:
            properties = user.user_properties.all()
            user_investment = self.model.objects.filter(user=user).first()
            {
                "overall_investment": 0,
                "total_invested_in_rental_assests": 0,
                "total_invested_in_non_rental_assests": 0,
                "total_earned_through_rental": 0,
                "total_earned_through_valuation": 0,
                "total_properties_invested": 0,
                "properties": [ {
                    "id" : 1,
                    "name" : "",
                    "return_type": "",
                    "address" : "",
                    "location" : "",
                    "description" : "",
                    "investment_amount" : 0,
                    "return_amount" : 0,
                    "current_valuation" : 0,
                    "investments": [
                    {
                        "id": 1,
                        "amount": 1000,
                        "created_at": "2021-06-15T12:00:00Z"
                    },
                    {
                        "id": 2,
                        "amount": 2000,
                        "created_at": "2021-06-15T12:00:00Z"
                    }
                    ],
                    "withdrawals": [
                    {
                        "id": 1,
                        "amount": 100,
                        "created_at": "2021-06-15T12:00:00Z"
                    },
                    {
                        "id": 2,
                        "amount": 200,
                        "created_at": "2021-06-15T12:00:00Z"
                    }
                    ],
                    "returns": [
                    {
                        "id": 1,
                        "amount": 100,
                        "created_at": "2021-06-15T12:00:00Z"
                    },
                    {
                        "id": 2,
                        "amount": 200,
                        "created_at": "2021-06-15T12:00:00Z"
                    }
                    ],
                    "valuation_hsitory" : [
                    {
                        "id": 1,
                        "amount": 1000,
                        "created_at": "2021-06-15T12:00:00Z"
                    },
                    {
                        "id": 2,
                        "amount": 2000,
                        "created_at": "2021-06-15T12:00:00Z"
                    }
                    ]
            } ]
            }
            # investments
