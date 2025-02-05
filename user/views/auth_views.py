from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from user.serializers.auth_serializers import GenerateAuthTokenSerializer
from user.serializers.email_serializers import (ChangePasswordSerializer,
                                                EmailSerializer)
from user.services.auth_services import GenerateAuthTokenService
from user.services.email_services import EmailService, ResetPasswordService


class GenerateAuthTokenViews(BaseAPIView):
    def __init__(self):
        self.service = GenerateAuthTokenService()

    @validate_request(GenerateAuthTokenSerializer)
    def get(self, request, data):
        service_data = self.service.get_service(request, data)
        response, status_code = self.get_response_or_error(service_data)
        return self.success(response, status_code)


class VerifyEmail(BaseAPIView):
    def __init__(self):
        self.service = EmailService()

    @auth_guard()
    @validate_request(EmailSerializer)
    def post(self, request, data, *args):
        service_data = self.service.verify_otp_email(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.success(response, code)


class SendEmailOTP(BaseAPIView):
    def __init__(self):
        self.service = EmailService()

    @auth_guard()
    @validate_request(EmailSerializer)
    def post(self, request, data, *args):
        service_date = self.service.send_otp_email(request, data)
        response, code = self.get_response_or_error(service_date)
        return self.success(response, code)


class ResetPassword(BaseAPIView):
    def __init__(self):
        self.service = ResetPasswordService()

    @validate_request(EmailSerializer)
    def post(self, request, data, *args):
        service_data = self.service.post_service(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.success(response, code)


class ChangePassword(BaseAPIView):
    def __init__(self):
        self.service = ResetPasswordService()

    @validate_request(ChangePasswordSerializer)
    def post(self, request, data, *args):
        service_data = self.service.reset_password(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.success(response, code)
