from rest_framework import serializers

from property.models.property import Property


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        exclude = ("is_deleted",)

