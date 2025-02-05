from rest_framework import serializers

from property.models.property_valuation_history import PropertyValuationHistory


class PropertyValuationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyValuationHistory
        exclude = ("is_deleted", "property", "meta", "id")
