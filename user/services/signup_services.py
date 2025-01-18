from common.boilerplate.auth.jwt_service import JWTService
from common.boilerplate.auth.password_handler import PasswordHandler
from common.boilerplate.services.base_service import BaseService
from user.helpers.django_password_validator import validate_user_password
from user.models.user import User
from user.models.user_token import UserToken
from django.utils import timezone

class SignUpServices(BaseService):
    def __init__(self):
        self.user_model = User
        self.user_token_model = UserToken
        self.token_service = JWTService()
        self.pw_handler = PasswordHandler()

    def post_service(self, request, data):
        if not validate_user_password(password=data.get("password")):
            return self.bad_request("Password does not meet the requirements")
        pwd = self.pw_handler.hash_pw(data.get("password"))
        if data.get("country_code") is not None:
            data["country_code"] = data.get("country_code").replace("+", "")
        if data.get("phone_number") and data.get("country_code"):
            if self.user_model.objects.filter(
                    phone_number=data.get("phone_number"),
                    country_code=data.get("country_code"),
                    is_deleted=False,
                ).exists():
                return self.bad_request(
                    "User already exists or Phone number already registered"
                )
        if data.get("username"):
            if self.user_model.objects.filter(
                username=data.get("username"), is_deleted=False
            ).first():
                return self.bad_request("Username already exists")
        if data.get("email"):
            if self.user_model.objects.filter(
                    email=data.get("email"), is_deleted=False
                ).exists():
                return self.bad_request("Email already exists")
        user_ins = self.user_model.objects.create(
            username=data.get("username"),
            password=pwd,
            phone_number=data.get("phone_number", None),
            country_code=data.get("country_code", None),
            email=data.get("email", None),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
        )
        token, exp = self.token_service.create_token(user=user_ins)
        token_ins = self.user_token_model.objects.create(
            user=user_ins, token=token, expiry=exp
        )
        user_ins.last_login = timezone.now()
        user_ins.save()
        return self.ok(
            {
                "token": token_ins.token,
                "username": user_ins.username,
                "country_code": user_ins.country_code,
                "phone_number": user_ins.phone_number,
                "email": user_ins.email,
                "is_email_verified" : user_ins.is_email_verified,
                "is_admin" : user_ins.is_admin,
                "is_phone_verified" : user_ins.is_phone_verified,
                "is_email_verified" : user_ins.is_email_verified
            }
        )
