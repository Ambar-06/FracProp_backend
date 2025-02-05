from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from user.serializers.user_profile_serializers import UserProfileSerializer
from user.services.user_profile_services import UserProfileService


class UserProfileView(BaseAPIView):
    def __init__(self):
        self.service = UserProfileService()

    @auth_guard()
    def get(self, request, data, *args):
        response = self.service.get_service(request, data)
        response, code = self.get_response_or_error(response)
        return self.success(response, code=code)

    @auth_guard()
    @validate_request(UserProfileSerializer)
    def patch(self, request, data, *args):
        response = self.service.patch_service(request, data)
        response, code = self.get_response_or_error(response)
        return self.success(response, code=code)
