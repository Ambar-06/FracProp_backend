import secrets

from user.models.otp import OTP
from user.models.user import User

class GenerateOTP:
    def __init__(self):
        self.user_model = User
        self.model = OTP

    def generate_otp(self, user_id):
        otp = secrets.randbelow(9000) + 1000
        user = User.objects.filter(uuid=user_id).first()
        self.model.objects.create(user=user, otp=otp)
        return otp
    
    def verify_otp(self, otp_obj):
        if not otp_obj:
            return False
        if otp_obj.is_valid:
            otp_obj.is_used = True
            otp_obj.save()
            user = otp_obj.user
            user.is_email_verified = True
            user.save()
            return True
        return False