import json
from rest_framework import serializers

from common.helpers.constants import (PropertyTypeDictionary,
                                      ReturnTypeDictionary)
from property.models.property import Property
from property.serializers.property_serializers import AmenitiesSerializer, OtherDetailsSerializer


class SinglePropertyFilterSerializer(serializers.Serializer):
    property_id = serializers.UUIDField(required=True)
    name = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    type = serializers.ChoiceField(choices=PropertyTypeDictionary, required=False)
    city = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    pin_code = serializers.CharField(required=False)
    govt_allotted_property_id = serializers.CharField(required=False)
    number_of_floors = serializers.IntegerField(required=False, min_value=0)
    number_of_rooms = serializers.IntegerField(required=False, min_value=0)
    return_type = serializers.ChoiceField(choices=ReturnTypeDictionary, required=False)
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
    amenities = AmenitiesSerializer(required=False)
    property_images = serializers.ListField(child=serializers.ImageField(), required=False, allow_empty=True)
    delete_images = serializers.ListField(child=serializers.URLField(), required=False, allow_empty=True)

    def to_internal_value(self, data):
        """Convert JSON string fields into Python dictionaries before validation."""
        if "delete_images" in data:
            if isinstance(data["delete_images"], str):
                try:
                    data["delete_images"] = json.loads(data["delete_images"])
                except json.JSONDecodeError:
                    raise serializers.ValidationError("Invalid JSON format for delete_images")
        json_fields = [field.name for field in Property._meta.fields if field.get_internal_type() == "JSONField"]

        for field in json_fields:
            if field in data and isinstance(data[field], str):
                try:
                    data[field] = json.loads(data[field])
                except json.JSONDecodeError:
                    raise serializers.ValidationError({field: "Invalid JSON format"})
        if "property_images" in data:
            if data["property_images"] and len(data["property_images"]) > 0:
                value = data["property_images"]
                if not isinstance(value, list):
                    raise serializers.ValidationError("Invalid format. Expected a list of images.")

                for file in value:
                    if not hasattr(file, 'file'):
                        raise serializers.ValidationError(f"Invalid file: {file}.")

        return super().to_internal_value(data)