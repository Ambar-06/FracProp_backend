from rest_framework import serializers


class PropertyInvestmentSerializer(serializers.Serializer):
    property_id = serializers.UUIDField()
    amount = serializers.FloatField(required=True, error_messages={"required": "Amount is required"})
