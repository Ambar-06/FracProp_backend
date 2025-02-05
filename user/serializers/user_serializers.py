from rest_framework import serializers

from user.models.user import User


class UserSerializer(serializers.Serializer):

    username = serializers.CharField(
        required=True,
        allow_blank=False,
        allow_null=False,
        error_messages={"required": "Username is required"},
    )
    password = serializers.CharField(
        required=True,
        allow_blank=False,
        allow_null=False,
        error_messages={"required": "Password is required"},
    )
    phone_number = serializers.CharField(
        required=True,
        allow_blank=False,
        allow_null=False,
        error_messages={"required": "Phone number is required"},
    )
    is_active = serializers.BooleanField(
        required=True,
        allow_null=False,
        error_messages={"required": "is_active is required"},
    )


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "uuid",
            "first_name",
            "last_name",
            "username",
            "phone_number",
            "country_code",
            "is_active",
            "is_admin",
            "is_phone_verified",
            "email",
            "is_email_verified",
        ]
