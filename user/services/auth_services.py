from common.boilerplate.auth.jwt_service import JWTService
from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from frac_prop import settings
from user.models.user import User

class GenerateAuthTokenService(BaseService):
    def __init__(self):
        self.user_model = User
        self.jwt_service = JWTService()

    def get_service(self, request, data):
        user_ins = self.user_model.objects.filter(email=data.get("email")).first()
        token = self.jwt_service.create_token(user_ins, expiry=int(settings.JWT_TOKEN_EXPIRY_IN_DAYS))
        return self.ok({"token": token}, StatusCodes().SUCCESS)