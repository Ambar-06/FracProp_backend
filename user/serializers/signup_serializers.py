from rest_framework import serializers

from user.models import User


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        allow_null=False,
        error_messages={
            "required": "Username is required",
            "null": "Username cannot be null",
        },
    )
    password = serializers.CharField(
        required=True,
        allow_null=False,
        error_messages={
            "required": "Password is required",
            "null": "Password cannot be null",
        },
    )
    confirm_password = serializers.CharField(
        required=True,
        allow_null=False,
        error_messages={
            "required": "Confirm password is required",
            "null": "Confirm password cannot be null",
        },
    )
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

    def validate(self, data):
        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError(
                "Password and confirm password does not match"
            )
        if not data.get("email") and not data.get("phone_number"):
            raise serializers.ValidationError(
                "Either email or Phone number is required to signup"
            )
        if data.get("phone_number"):
            if not data.get("country_code"):
                raise serializers.ValidationError("Country code is required")
            if not data.get("country_code").startswith("+"):
                raise serializers.ValidationError("Phone number should start with +")

            if len(data.get("phone_number")) < 9:
                raise serializers.ValidationError(
                    "Phone number should be of 9 digits minimum"
                )
            if not data.get("phone_number").isdigit():
                raise serializers.ValidationError("Phone number should be numeric")
            if User.objects.filter(
                phone_number=data.get("phone_number"),
                country_code=data.get("country_code"),
            ).exists():
                raise serializers.ValidationError("Phone number already exists")
        if User.objects.filter(username=data.get("username")).exists():
            raise serializers.ValidationError("Username already exists")
        return data
