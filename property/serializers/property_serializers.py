from rest_framework import serializers

from property.models.property import Property
from common.helpers.constants import BuildingHealthDictionary, PropertyTypeDictionary

class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        exclude = ("is_deleted",)


class OtherDetailsSerializer(serializers.Serializer):
    
        construction_age_in_years = serializers.IntegerField(required=True, min_value=0, max_value=100)
        building_health = serializers.ChoiceField(required=True, choices=BuildingHealthDictionary)

class PropertyFilterSerializer(serializers.Serializer):

    name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    state = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    pin_code = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    type = serializers.ChoiceField(choices=PropertyTypeDictionary, required=True)
    number_of_floors = serializers.IntegerField(required=True, min_value=0)
    built_area_in_sqft = serializers.FloatField(required=True)
    area_in_sqft = serializers.FloatField(required=True)
    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)
    valuation = serializers.FloatField(required=True)
    has_loan = serializers.BooleanField(required=False, default=False)
    is_verified = serializers.BooleanField(required=False, default=False)
    is_approved = serializers.BooleanField(required=False, default=False)
    is_active = serializers.BooleanField(required=False, default=True)
    other_details = OtherDetailsSerializer(required=True)

    # def validate(self, data):
    #     if data.get("type") not in [i[0] for i in Property.PROPERTY_TYPE_CHOICES]:
    #         raise serializers.ValidationError("Invalid property type")
    #     return data
