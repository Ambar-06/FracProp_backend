from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.api.base_paginated_api import PaginatedBaseApiView
from common.boilerplate.api.custom_pagination import CustomPagination
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from user.serializers.login_serializers import LoginSerializer
from user.serializers.signup_serializers import SignUpSerializer
from user.serializers.single_user_serializers import SingleUserSerializer
from user.serializers.user_serializers import UserViewSerializer
from user.services.login_services import LoginServices
from user.services.signup_services import SignUpServices
from user.services.single_user_services import SingleUserServices
from user.services.user_services import UserServices


class UserSignUp(BaseAPIView):
    def __init__(self):
        self.service = SignUpServices()

    @validate_request(SignUpSerializer)
    def post(self, request, data, *args):
        data = request.data
        response = self.service.post_service(request, data)
        response, code = self.get_response_or_error(response)
        return self.success(response, code=code)


class UserLogin(BaseAPIView):
    def __init__(self):
        self.service = LoginServices()

    @validate_request(LoginSerializer)
    def post(self, request, data, *args):
        data = request.data
        response = self.service.post_service(request, data)
        response, code = self.get_response_or_error(response)
        return self.success(response, code=code)


class UserView(BaseAPIView, PaginatedBaseApiView):
    def __init__(self):
        super().__init__(
            serializer_class=UserViewSerializer,
            pagination_class=CustomPagination,
        )
        self.service = UserServices()

    @auth_guard(admin=True)
    def get(self, request, data, *args):
        response = self.service.get_service(request, data)
        self.queryset, code = self.get_response_or_error(response)
        return self.success_paginated(
            page=request.query_params.get("page", 1),
            perPage=request.query_params.get("perPage", 10),
        )

    # @auth_guard(admin=True)
    # @validate_request(UserSerializer)
    # def post(self, request, data, *args):
    #     response = self.service.post_service(request, data)
    #     response, code = self.get_response_or_error(response)
    #     return self.success(response, code=code)
    

class SingleUserView(BaseAPIView):
    def __init__(self):
        self.service = SingleUserServices()

    @auth_guard(admin=True)
    @validate_request(SingleUserSerializer)
    def get(self, request, data, *args):
        response = self.service.get_service(request, data)
        response, code = self.get_response_or_error(response)
        return self.success(response, code=code)

    @auth_guard(admin=True)
    @validate_request(SingleUserSerializer)
    def patch(self, request, data, *args):
        response = self.service.patch_service(request, data)
        response, code = self.get_response_or_error(response)
        return self.success(response, code=code)

    @auth_guard(admin=True)
    @validate_request(SingleUserSerializer)
    def delete(self, request, data, *args):
        response = self.service.delete_service(request, data)
        response, code = self.get_response_or_error(response)
        return self.success(response, code=code)