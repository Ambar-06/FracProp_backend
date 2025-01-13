from user.models.user import User


class LoginRequestValidator:
    def __init__(self):
        self.user_model = User

    def validate_login_request(self, data):
        if data.get("username"):
            user = self.user_model.objects.get(
                username=data.get("username"), is_active=True, is_deleted=False
            )
            if not user:
                return False, "Incorrect username or User does not exist"
        if data.get("email"):
            user = self.user_model.objects.filter(
                email=data.get("email"), is_active=True, is_deleted=False
            ).first()
            if not user:
                return False, "Incorrect email or User does not exist"
        if data.get("phone_number"):
            country_code = data.get("country_code").replace("+", "")
            user = self.user_model.objects.get(
                phone_number=data.get("phone_number"),
                country_code=country_code,
                is_active=True,
                is_deleted=False,
            )
            if not user:
                return False, "Incorrect phone number or User does not exist"
        return True, user
