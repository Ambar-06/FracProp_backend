from rest_framework import serializers

from property.models.property import Property


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        exclude = ("is_deleted",)


class PropertyFilterSerializer(serializers.Serializer):

    name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    type = serializers.ChoiceField(choices=Property.PROPERTY_TYPE_CHOICES)
    number_of_floors = serializers.IntegerField(required=True, min_value=0)
    built_area_in_sqft = serializers.FloatField(required=True)
    area_in_sqft = serializers.FloatField(required=True)
    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)
    has_loan = serializers.BooleanField(default=False)
    is_verified = serializers.BooleanField(default=False)
    is_approved = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=True)
    other_details = serializers.JSONField(required=False)

    def validate(self, data):
        if data.get("type") not in [i[0] for i in Property.PROPERTY_TYPE_CHOICES]:
            raise serializers.ValidationError("Invalid property type")
        return data
