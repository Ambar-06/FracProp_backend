from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from payment.models.transaction import Transaction
from user.models.user import User


class TransactionServices(BaseService):
    def __init__(self):
        pass

    def get_service(self, request, data):
        user_id = request.user.get("uuid")
        user = User.objects.filter(uuid=user_id).first()
        transaction_data = Transaction.objects.filter(user=user).order_by("-created_at")
        if data.get("start_date"):
            transaction_data = transaction_data.filter(created_at__gte=data.get("start_date"))
        if data.get("end_date"):
            transaction_data = transaction_data.filter(created_at__lte=data.get("end_date"))
        if data.get("amount"):
            transaction_data = transaction_data.filter(amount=data.get("amount"))
        return self.ok(transaction_data, StatusCodes().SUCCESS)