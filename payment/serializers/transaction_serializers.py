from rest_framework import serializers

from payment.models.transaction import Transaction

class TransactionFilterSerializer(serializers.Serializer):
    end_date = serializers.DateField(required=False)
    start_date = serializers.DateField(required=False)
    amount = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)

class TransactionViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'