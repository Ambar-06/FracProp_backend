from rest_framework import serializers

class SingleWishlistSerializer(serializers.Serializer):
    wishlist_id = serializers.UUIDField(required=True)