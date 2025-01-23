from rest_framework import serializers

class UserProfileSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=False,
        allow_null=True,
    )
    phone_number = serializers.CharField(
        required=False,
        allow_null=True,
    )
    country_code = serializers.CharField(
        required=False,
        allow_null=True,
    )
    first_name = serializers.CharField(
        required=False,
        allow_null=True,
    )
    last_name = serializers.CharField(
        required=False,
        allow_null=True,
    )