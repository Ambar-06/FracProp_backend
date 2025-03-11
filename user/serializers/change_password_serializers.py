from rest_framework import serializers

class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get("new_password") != attrs.get("confirm_password"):
            raise serializers.ValidationError("Passwords do not match")
        return attrs