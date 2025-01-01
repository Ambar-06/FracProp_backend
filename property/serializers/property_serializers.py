from rest_framework import serializers

from property.models.property import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"

    def create(self, validated_data):
        return Property.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["type"] = instance.get_type_display()
        return response
