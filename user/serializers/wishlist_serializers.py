from rest_framework import serializers


class WishlistSerializer(serializers.Serializer):
    user_id = serializers.UUIDField()
    property_id = serializers.UUIDField()
