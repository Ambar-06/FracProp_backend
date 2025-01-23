from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    password = serializers.CharField(
        required=True,
        allow_null=False,
        error_messages={
            "required": "Password is required",
            "null": "Password cannot be null",
        },
    )
    email = serializers.EmailField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    country_code = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    phone_number = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )

    def validate(self, data):
        if not data.get("phone_number") and not data.get("email") and not data.get("username"):
            raise serializers.ValidationError(
                "Either username or email or Phone number is required to login"
            )
        if data.get("phone_number"):
            if not data.get("country_code"):
                raise serializers.ValidationError("Country code is required")
            if len(data.get("phone_number")) < 9:
                raise serializers.ValidationError(
                    "Phone number should be of 9 digits minimum"
                )
            if not data.get("country_code").startswith("+"):
                raise serializers.ValidationError("Country Code should start with +")
        return data
