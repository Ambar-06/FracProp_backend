from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
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
