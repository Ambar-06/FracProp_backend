from rest_framework import serializers
from common.helpers.constants import BuildingHealthDictionary, PropertyTypeDictionary, ReturnTypeDictionary
from property.serializers.property_serializers import OtherDetailsSerializer

class SinglePropertyFilterSerializer(serializers.Serializer):
    property_id = serializers.UUIDField(required=True)
    name = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    type = serializers.ChoiceField(
        choices=PropertyTypeDictionary, required=False
    )
    city = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    pin_code = serializers.CharField(required=False)
    govt_allotted_property_id = serializers.CharField(required=False)
    number_of_floors = serializers.IntegerField(required=False, min_value=0)
    number_of_rooms = serializers.IntegerField(required=False, min_value=0)
    return_type = serializers.ChoiceField(
        choices=ReturnTypeDictionary, required=False
    )
    built_area_in_sqft = serializers.FloatField(required=False)
    valuation = serializers.FloatField(required=False)
    area_in_sqft = serializers.FloatField(required=False)
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)
    has_loan = serializers.BooleanField(required=False)
    is_verified = serializers.BooleanField(required=False)
    is_approved = serializers.BooleanField(required=False)
    is_active = serializers.BooleanField(required=False)
    other_details = OtherDetailsSerializer(required=False)
