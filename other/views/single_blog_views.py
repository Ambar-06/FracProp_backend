from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from other.serializers.single_blog_serializers import SingleBlogSerializer
from other.services.single_blog_services import SingleBlogService


class SingleBlogView(BaseAPIView):
    def __init__(self):
        self.service = SingleBlogService()

    @auth_guard()
    @validate_request(SingleBlogSerializer)
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.response(response, code)

    @auth_guard(admin=True)
    @validate_request(SingleBlogSerializer)
    def patch(self, request, data, *args):
        service_data = self.service.patch_service(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.response(response, code)
