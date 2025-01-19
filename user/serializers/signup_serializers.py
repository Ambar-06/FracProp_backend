from rest_framework import serializers
from user.models import User

class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        allow_null=False,
        error_messages={
            "required": "First name is required",
            "null": "First name cannot be null",
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
        required=True,
        allow_null=False,
        error_messages={
            "required": "Email is required",
            "null": "Email cannot be null",
        },
    )
    phone_number = serializers.CharField(
        required=True,
        allow_null=False,
        error_messages={
            "required": "Phone number is required",
            "null": "Phone number cannot be null",
        },
    )

    def validate(self, data):
        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError("Password and confirm password does not match")
        if not data("email") and not data.get("phone_number"):
            raise serializers.ValidationError("Either email or Phone number is required to signup")
        if data.get("phone_number"):
            if "+" in data.get("phone_number"):
                if "-" in data.get("phone_number"):
                    country_code, number = data.get("phone_number")[1:].split("-")
                else:
                    raise serializers.ValidationError("Phone number should be in format +91-1234567890")
                if len(number) < 9:
                    raise serializers.ValidationError("Phone number should be of 9 digits minimum")
                if not number.isdigit():
                    raise serializers.ValidationError("Phone number should be numeric")
                # if number[0] != "7" and number[0] != "8" and number[0] != "9" and number[0] != "9":
                #     raise serializers.ValidationError("Phone number should start with 7, 8 or 9")
                if User.objects.filter(phone_number=number).exists() or User.objects.filter(phone_number=data.get("phone_number")).exists():
                    raise serializers.ValidationError("Phone number already exists")
            else:
                raise serializers.ValidationError("Phone number should start with +")
        if User.objects.filter(username=data.get("username")).exists():
            raise serializers.ValidationError("Username already exists")
        return data