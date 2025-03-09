from rest_framework import serializers

class TwoFactorFilterSerializer(serializers.Serializer):
    otp = serializers.CharField(
        required=True,
        allow_blank=False,
        allow_null=False,
        error_messages={"required": "OTP is required"},
    )