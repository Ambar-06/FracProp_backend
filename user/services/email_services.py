from common.boilerplate.auth.password_handler import PasswordHandler
from common.boilerplate.secrets.random_id_generator import generate_random_id_number
from user.models.otp import OTP
from user.models.user_password_management import PasswordManagementUser
from user.helpers.verification_helper import EmailHelper
from common.boilerplate.secrets.otp import GenerateOTP
from common.boilerplate.services.base_service import BaseService
from user.models.user import User
from common.helpers.constants import EmailTypes

class EmailService(BaseService):
    def __init__(self):
        self.user_model = User
        self.otp_helper = GenerateOTP()
        self.email_helper = EmailHelper()
        self.otp_model = OTP

    def send_otp_email(self, request, data):
        user_id = request.user.get("uuid")
        user = self.user_model.objects.filter(uuid=user_id).first()
        if not user:
            return self.not_found("User not found")
        if self.user_model.objects.filter(email=data.get("email"), is_active=True).exclude(uuid=user_id).exists():
            return self.bad_request("Email already exists and belongs to another user")
        user.email = data.get("email")
        user.save()
        otp = self.otp_helper.generate_otp(user.uuid)
        resp = self.email_helper.send_template_email(template_type=EmailTypes().OTP, otp=otp, user=user)
        if resp:
            return self.ok("OTP sent successfully")
        return self.bad_request("Failed to send OTP")
    
    def verify_otp_email(self, request, data):
        user_id = request.user.get("uuid")
        user = self.user_model.objects.filter(uuid=user_id).first()
        otp_obj = self.otp_model.objects.filter(otp=data.get("otp"), user=user, is_used=False).first()
        if otp_obj is None:
            return self.bad_request("OTP is invalid")
        if not self.otp_helper.verify_otp(otp_obj):
            return self.bad_request("OTP is invalid")
        return self.ok("OTP verified successfully")
    
class ResetPasswordService(BaseService):
    def __init__(self):
        self.user_model = User
        self.pass_manager_model = PasswordManagementUser
        self.email_helper = EmailHelper()
        self.pw_handler = PasswordHandler()

    def post_service(self, request, data):
        email = data.get("email")
        user = self.user_model.objects.filter(email=email).first()
        if not user:
            return self.not_found("User not found with the given email")
        random_str = generate_random_id_number(use_small_letters=True)
        user_id_str = str(user.uuid)
        random_str = random_str + "-" + user_id_str[:5]
        url = data.get("reset_password_url")
        reset_url = url + "?s=" + random_str + "&m=" + email
        self.pass_manager_model.objects.create(
            user=user,
            unique_token=random_str,
            link_generated=f"{reset_url}"
        )
        resp = self.email_helper.send_template_email(template_type=EmailTypes().RESET_PASSWORD, link=reset_url, user=user)
        if resp:
            return self.ok("Reset password link sent successfully")
        return self.bad_request("Failed to send reset password link")
    
    def reset_password(self, request, data):
        code = data.get("code")
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        email = data.get("email")
        if password != confirm_password:
            return self.bad_request("Password and confirm password does not match")
        pass_manager = self.pass_manager_model.objects.filter(unique_token=code).first()
        if pass_manager.is_used:
            return self.bad_request("Reset password code is already used")
        ut = pass_manager.unique_token
        user = self.user_model.objects.filter(email=email).first()
        if not user:
            return self.not_found("Email not found in the database")
        user_id = str(user.uuid)
        if user_id[:5] != ut.split("-")[1]:
            return self.bad_request("Invalid reset password code")
        user.password = self.pw_handler.hash_pw(data.get("password"))
        user.save()
        pass_manager.is_used = True
        pass_manager.save()
        return self.ok("Password reset successfully")


        

