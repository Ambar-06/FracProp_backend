from jose import jwt
from datetime import datetime, timedelta
from frac_prop import settings

"""
This class is used for JWT
Fields:
    JWT_SECRET: Secret for JWT
Methods:
    create_token: This method is used for creating a new JWT token
    verify_token: This method is used for verifying a JWT token
WorkFlow:
    First we create a payload
    Then we create a token
    Then we return the token
"""


class JWTService:
    JWT_SECRET = settings.JWT_SECRET

    def create_token(self, user, expiry=None):
        if expiry is None:
            expiry = int(settings.JWT_TOKEN_EXPIRY_IN_DAYS)
        exp = datetime.now() + timedelta(days=expiry)
        payload = {
            "sub": str(user.uuid),
            "iat": datetime.now(),
            "exp": exp,
        }
        token = jwt.encode(payload, JWTService.JWT_SECRET, settings.JWT_ALGORITHM)
        return token, exp

    def verify_token(self, jwt_token):
        jwt_payload = jwt.decode(
            jwt_token, JWTService.JWT_SECRET, settings.JWT_ALGORITHM
        )
        return jwt_payload


def generate_secret():
    import secrets

    return secrets.token_urlsafe(32)
