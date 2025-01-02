from rest_framework import serializers

from property.models.property import Property


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = "__all__"

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        property_obj = Property.objects.create(**validated_data)
        return property_obj

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response
