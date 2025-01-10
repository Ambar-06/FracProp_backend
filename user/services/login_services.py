from common.boilerplate.auth.jwt_service import JWTService
from common.boilerplate.auth.password_handler import PasswordHandler
from common.boilerplate.services.base_service import BaseService
from user.models.user import User
from django.utils import timezone
from user.models.user_token import UserToken


class LoginServices(BaseService):
    def __init__(self):
        self.jwt_service = JWTService()
        self.password_handler = PasswordHandler()
        self.user_model = User
        self.user_token = UserToken

    def post_service(self, request, data):
        user = self.user_model.objects.filter(
            username=data.get("username"), is_active=True, is_deleted=False
        ).first()
        if not user:
            return self.bad_request("Incorrect username or User does not exist")
        if not self.password_handler.is_password_valid(
            data.get("password"), user.password
        ):
            return self.bad_request("Invalid credentials")
        token, expiry = self.jwt_service.create_token(user=user)
        token_obj = self.user_token.objects.filter(user=user).first()
        token_obj.token = token
        token_obj.expiry = expiry
        token_obj.save()
        user.last_login = timezone.now()
        user.save()
        return self.ok(
            {
                "token": token,
                "username": user.username,
                "country_code": user.country_code,
                "phone_number": user.phone_number,
                "email": user.email,
                "is_email_verified" : user.is_email_verified,
                "is_admin": user.is_admin,
                "is_phone_verified": user.is_phone_verified,
                "is_email_verified" : user.is_email_verified
            }
        )
