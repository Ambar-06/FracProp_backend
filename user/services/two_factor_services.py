from common.boilerplate.auth.two_factor_authentication import TwoFactorAuthentication
from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from user.models.user import User


class TwoFactorServices(BaseService):
    def __init__(self):
        self.authenticator = TwoFactorAuthentication()

    def get_service(self, request, data):
        user_id = request.user.get("uuid")
        user = User.objects.filter(uuid=user_id).first()
        _, key, path = self.authenticator.generate_qr_code(user.username)
        base_url = f"{request.scheme}://{request.get_host()}"
        qr_url = f"{base_url}/{path.lstrip('/')}"
        user.secret_key = key
        user.save()
        return self.ok({"qr_url": qr_url}, StatusCodes().SUCCESS)
        

    def post_service(self, request, data):
        user_id = request.user.get("uuid")
        user = User.objects.filter(uuid=user_id).first()
        if not self.authenticator.verify_totp(user.secret_key, data.get("otp")):
            return self.bad_request("Invalid OTP")
        user.is_two_factor_enabled = True
        user.save()
        return self.ok("Two factor authentication enabled successfully", StatusCodes().SUCCESS)