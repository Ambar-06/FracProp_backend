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

    def validate(self, attrs):
        if not attrs.get("email") and not attrs.get("phone_number"):
            raise serializers.ValidationError(
                "Either email or Phone number is required to update profile"
            )
        if attrs.get("phone_number"):
            if not attrs.get("country_code"):
                raise serializers.ValidationError("Country code is required")
            if not attrs.get("country_code").startswith("+"):
                raise serializers.ValidationError("Country code should start with +")
            if len(attrs.get("phone_number")) < 9:
                raise serializers.ValidationError(
                    "Phone number should be of 9 digits minimum"
                )
        return attrs