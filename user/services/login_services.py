from common.boilerplate.auth.jwt_service import JWTService
from common.boilerplate.auth.password_handler import PasswordHandler
from common.boilerplate.services.base_service import BaseService
from user.helpers.login_request_helper import LoginRequestValidator
from user.models.user import User
from django.utils import timezone
from user.models.user_token import UserToken


class LoginServices(BaseService):
    def __init__(self):
        self.jwt_service = JWTService()
        self.password_handler = PasswordHandler()
        self.user_model = User
        self.user_token = UserToken
        self.validator = LoginRequestValidator()

    def post_service(self, request, data):
        is_valid, obj_or_msg = self.validator.validate_login_request(data)
        if not is_valid:
            return self.bad_request(obj_or_msg)
        if not self.password_handler.is_password_valid(
            data.get("password"), obj_or_msg.password
        ):
            return self.bad_request("Invalid credentials")
        token, expiry = self.jwt_service.create_token(user=obj_or_msg)
        token_obj = self.user_token.objects.filter(user=obj_or_msg).first()
        if token_obj is None:
            token_obj = self.user_token.objects.create(
                user_id=str(obj_or_msg._id), token=token, expiry=expiry
            )
        else:
            token_obj.token = token
            token_obj.expiry = expiry
            token_obj.save()
        obj_or_msg.last_login = timezone.now()
        obj_or_msg.save()
        # wallet_ins = self.wallet_model.objects.filter(
        #     user_id=str(obj_or_msg._id)
        # ).first()
        return self.ok(
            {
                "token": token,
                "username": obj_or_msg.username,
                "country_code": obj_or_msg.country_code,
                "phone_number": obj_or_msg.phone_number,
                "email": obj_or_msg.email,
                "is_email_verified": obj_or_msg.is_email_verified,
                "is_admin": obj_or_msg.is_admin,
                "is_phone_verified": obj_or_msg.is_phone_verified,
                "is_email_verified": obj_or_msg.is_email_verified,
            }
        )
