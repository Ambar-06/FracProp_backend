from rest_framework import serializers


class PropertyInvestmentSerializer(serializers.Serializer):
    property_id = serializers.UUIDField()
    amount = serializers.IntegerField()
