from investment.models.investment import Investment
from investment.models.investment_return import InvestmentReturn
from django.db.models import Sum

class InvestmentHelper:
    def __init__(self):
        pass

    def get_investment_data(self, user):
        user_properties = user.user_properties.all()
        property_data = []
        user_property_investment_qs = Investment.objects.filter(user=user).order_by('-created_at')
        invested_in_rental_assests = user_property_investment_qs.filter(property__return_type='RENTAL').aggregate(Sum('amount')).get('amount__sum', 0)
        invested_in_non_rental_assests = user_property_investment_qs.filter(property__return_type='VALUATION').aggregate(Sum('amount')).get('amount__sum', 0)
        total_earned_through_rental = InvestmentReturn.objects.filter(user=user, return_type='RENTAL').aggregate(Sum('return_in_amount')).get('return_in_amount__sum', 0)
        total_earned_through_valuation = InvestmentReturn.objects.filter(user=user, return_type='VALUATION').aggregate(Sum('return_in_amount')).get('return_in_amount__sum', 0)
        user_general_data = {
            "overall_investment" : user_property_investment_qs.aggregate(Sum('amount')).get('amount__sum', 0),
            "total_invested_in_rental_assests" : invested_in_rental_assests,
            "total_invested_in_non_rental_assests": invested_in_non_rental_assests,
            "total_earned_through_rental": total_earned_through_rental,
            "total_earned_through_valuation": total_earned_through_valuation,
            "total_properties_invested" : len(user_properties)
        }
        for user_property in user_properties:
            user_property_investment_qs = user_property_investment_qs.filter(property=user_property.property).order_by('-created_at')[:10]
            user_investment_return_qs = InvestmentReturn.objects.filter(user=user, property=user_property.property).order_by('-created_at')[:10]
            investment_amount = user_property_investment_qs.aggregate(Sum('amount')).get('amount__sum', 0)
            return_amount = user_investment_return_qs.aggregate(Sum('return_in_amount')).get('return_in_amount__sum', 0)
            property_valuation_data_qs = user_property.property.valuation_history.all().order_by('-created_at')[:10]
            property_data.append({
                "uuid": user_property.property.uuid,
                "name": user_property.property.name,
                "return_type": user_property.property.return_type,
                "address": user_property.property.address,
                "latitude": user_property.property.latitude,
                "longitude": user_property.property.longitude,
                "description": user_property.property.description,
                "number_of_floors" : user_property.property.number_of_floors,
                "built_area_in_sqft" : user_property.property.built_area_in_sqft,
                "area_in_sqft" : user_property.property.area_in_sqft,
                "number_of_rooms" : user_property.property.number_of_rooms,
                "current_valuation" : user_property.property.valuation,
                "investment_lock_in_period_in_months" : user_property.property.investment_lock_in_period_in_months,
                "has_loan" : user_property.property.has_loan,
                "is_verified" : user_property.property.is_verified,
                "investment_amount": investment_amount,
                "return_amount": return_amount,
                "investments": user_property_investment_qs.values_list('id', 'amount', 'created_at', flat=True),
                "withdrawals": [],
                "returns": user_investment_return_qs.values_list('id', 'return_in_amount', 'created_at', flat=True),
                "valuation_hsitory_of_last_10_months": property_valuation_data_qs.values_list('id', 'valuation', 'created_at', flat=True)
            })
        user_general_data["properties"] = property_data
        return user_general_data
