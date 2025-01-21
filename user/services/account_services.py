from common.boilerplate.services.base_service import BaseService
from common.helpers.encryption_decryption import encrypt
from user.models.bank_account_detail import BankAccountDetail
import random as _r

from user.models.user import User
from user.serializers.account_serializers import BankAccountDetailViewSerializer


class AccountServices(BaseService):
    def __init__(self):
        self.model = BankAccountDetail
        self.user_model = User

    def get_service(self, request, data):
        pass

    def post_service(self, request, data):
        user_id = request.user.get("uuid")
        user = self.user_model.objects.filter(uuid=user_id).first()
        if not user:
            return self.bad_request("User not found")
        key_serial = _r.randint(1, 5)  # nosec
        data["encryption_key_serial"] = key_serial
        account_number = data.pop("account_number", None)
        ifsc = data.pop("ifsc", None)
        data.pop("confirm_account_number", None)
        data["enctrypted_account_number"] = encrypt(account_number, serial=key_serial)
        data["encrypted_ifsc"] = encrypt(ifsc, serial=key_serial)
        data["user"] = user
        account_detail = self.model.objects.create(**data)
        return self.ok(BankAccountDetailViewSerializer(account_detail).data)
