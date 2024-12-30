from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    otp = serializers.IntegerField(required=False)
    reset_password_url = serializers.URLField(required=False)

class ChangePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    code = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)