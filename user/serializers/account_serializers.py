from rest_framework import serializers

from user.models.bank_account_detail import BankAccountDetail


class BankAccountDetailViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountDetail
        exclude = ("created_at", "encryption_key_serial")


class BankAccountDetailSerializer(serializers.Serializer):
    account_holder_name = serializers.CharField(required=True)
    account_number = serializers.CharField(required=True)
    confirm_account_number = serializers.CharField(required=True)
    ifsc = serializers.CharField(required=True)
    bank_name = serializers.CharField(required=True)
    branch_name = serializers.CharField(required=True)
    is_primary = serializers.BooleanField(required=False)

    def validate(self, data):
        if data["account_number"] != data["confirm_account_number"]:
            raise serializers.ValidationError(
                "Account number and confirm account number does not match"
            )
        return data
