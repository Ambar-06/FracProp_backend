from rest_framework import serializers

from property.models.property import Property

class SinglePropertyFilterSerializer(serializers.Serializer):
    property_id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    type = serializers.ChoiceField(choices=Property.PROPERTY_TYPE_CHOICES, required=False)
    number_of_floors = serializers.IntegerField(required=False, min_value=0)
    built_area_in_sqft = serializers.FloatField(required=False)
    area_in_sqft = serializers.FloatField(required=False)
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)
    has_loan = serializers.BooleanField(required=False)
    is_verified = serializers.BooleanField(required=False)
    is_approved = serializers.BooleanField(required=False)
    is_active = serializers.BooleanField(required=False)
    other_details = serializers.JSONField(required=False)