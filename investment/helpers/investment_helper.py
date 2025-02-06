from django.db.models import Sum

from investment.models.investment import Investment
from investment.models.investment_return import InvestmentReturn
from investment.models.transaction import Transaction
from property.models.user_property import UserProperty
from property.models.user_property_amount import UserPropertyAmount
from property.models.user_property_stake import UserPropertyStake


class InvestmentHelper:
    def __init__(self):
        pass

    def get_investment_data(self, user):
        user_properties = user.user_properties.filter(is_deleted=False)
        property_data = []
        user_property_investment_qs = Investment.objects.filter(user=user).order_by(
            "-created_at"
        )
        invested_in_rental_assests = (
            user_property_investment_qs.filter(property__return_type="RENTAL")
            .aggregate(Sum("amount"))
            .get("amount__sum", 0)
        )
        invested_in_non_rental_assests = (
            user_property_investment_qs.filter(property__return_type="VALUATION")
            .aggregate(Sum("amount"))
            .get("amount__sum", 0)
        )
        total_earned_through_rental = (
            InvestmentReturn.objects.filter(user=user, return_type="RENTAL")
            .aggregate(Sum("return_in_amount"))
            .get("return_in_amount__sum", 0)
        )
        total_earned_through_valuation = (
            InvestmentReturn.objects.filter(user=user, return_type="VALUATION")
            .aggregate(Sum("return_in_amount"))
            .get("return_in_amount__sum", 0)
        )
        user_general_data = {
            "overall_investment": user_property_investment_qs.aggregate(
                Sum("amount")
            ).get("amount__sum", 0),
            "total_invested_in_rental_assests": invested_in_rental_assests,
            "total_invested_in_non_rental_assests": invested_in_non_rental_assests,
            "total_earned_through_rental": total_earned_through_rental,
            "total_earned_through_valuation": total_earned_through_valuation,
            "total_properties_invested": len(user_properties),
        }
        for user_property in user_properties:
            user_property_investment_qs = user_property_investment_qs.filter(
                property=user_property.property
            ).order_by("-created_at")[:10]
            user_investment_return_qs = InvestmentReturn.objects.filter(
                user=user, property=user_property.property
            ).order_by("-created_at")[:10]
            investment_amount = user_property_investment_qs.aggregate(
                Sum("amount")
            ).get("amount__sum", 0)
            return_amount = user_investment_return_qs.aggregate(
                Sum("return_in_amount")
            ).get("return_in_amount__sum", 0)
            property_valuation_data_qs = (
                user_property.property.valuation_history.all().order_by("-created_at")[
                    :10
                ]
            )
            property_data.append(
                {
                    "uuid": user_property.property.uuid,
                    "name": user_property.property.name,
                    "return_type": user_property.property.return_type,
                    "address": user_property.property.address,
                    "latitude": user_property.property.latitude,
                    "longitude": user_property.property.longitude,
                    "description": user_property.property.description,
                    "number_of_floors": user_property.property.number_of_floors,
                    "built_area_in_sqft": user_property.property.built_area_in_sqft,
                    "area_in_sqft": user_property.property.area_in_sqft,
                    "number_of_rooms": user_property.property.number_of_rooms,
                    "current_valuation": user_property.property.valuation,
                    "investment_lock_in_period_in_months": user_property.property.investment_lock_in_period_in_months,
                    "has_loan": user_property.property.has_loan,
                    "is_verified": user_property.property.is_verified,
                    "investment_amount": investment_amount,
                    "return_amount": return_amount,
                    "investments": user_property_investment_qs.values_list(
                        "id", "amount", "created_at", flat=True
                    ),
                    "withdrawals": [],
                    "returns": user_investment_return_qs.values_list(
                        "id", "return_in_amount", "created_at", flat=True
                    ),
                    "valuation_hsitory_of_last_10_months": property_valuation_data_qs.values_list(
                        "id", "valuation", "created_at", flat=True
                    ),
                }
            )
        user_general_data["properties"] = property_data
        return user_general_data

    def perform_post_investment_operation(
        self, user, property, amount, percentage_transacted
    ):
        Investment.objects.create(
            user=user,
            property=property,
            amount=amount,
        )
        Transaction.objects.create(
            user=user,
            amount=amount,
            type="DEPOSIT",
        )
        self.create_or_update_user_investments(
            user, property, amount, percentage_transacted, is_deposit=True
        )
        UserProperty.objects.get_or_create(
            user=user, property=property, defaults={"user": user, "property": property}
        )

    def create_or_update_user_investments(
        self, user, property, amount, percentage_transacted, is_deposit=False
    ):
        user_property_amount = UserPropertyAmount.objects.filter(
            user=user, property=property
        ).first()
        if user_property_amount is None:
            user_property_amount = UserPropertyAmount.objects.create(
                user=user,
                property=property,
            )
        if is_deposit:
            user_property_amount.total_amount = (
                user_property_amount.total_amount + amount
                if user_property_amount.total_amount is not None
                else amount
            )
            user_property_amount.total_investment = (
                user_property_amount.total_investment + amount
                if user_property_amount.total_investment is not None
                else amount
            )
        else:
            user_property_amount.total_amount = (
                user_property_amount.total_amount - amount
            )
            user_property_amount.total_withdrawal = (
                user_property_amount.total_withdrawal + amount
                if user_property_amount.total_withdrawal is not None
                else amount
            )
        user_property_amount.save()
        user_investment_percentage = UserPropertyStake.objects.filter(
            user=user, property=property
        ).first()
        if user_investment_percentage is None:
            user_investment_percentage = UserPropertyStake.objects.create(
                user=user, property=property
            )
        if is_deposit:
            user_investment_percentage.stake_in_percent = (
                float(user_investment_percentage.stake_in_percent) + float(percentage_transacted)
                if user_investment_percentage.stake_in_percent is not None
                else float(percentage_transacted)
            )
        else:
            user_investment_percentage.stake_in_percent = (
                float(user_investment_percentage.stake_in_percent) - float(percentage_transacted)
            )
        user_investment_percentage.save()

        return user_property_amount, user_investment_percentage
