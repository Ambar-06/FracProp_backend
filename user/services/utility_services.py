from common.boilerplate.auth.password_handler import PasswordHandler
from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from user.models.user import User


class ChangePasswordService(BaseService):
    def __init__(self):
        self.model = User
        self.password_helper = PasswordHandler()

    def post_service(self, request, data):
        user_id = request.user.get("uuid")
        user = self.model.objects.filter(uuid=user_id).first()
        current_password = data.get("current_password")
        if self.password_helper.is_password_valid(current_password, user.password):
            user.password = self.password_helper.hash_pw(data.get("new_password"))
            user.save()
            return self.ok("Password changed successfully", StatusCodes().SUCCESS)
        return self.bad_request("Incorrect Current Password")