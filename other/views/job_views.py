from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.api.custom_pagination import CustomPagination
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from other.serializers.job_serializers import JobFilterSerializer, JobViewSerializer
from other.services.job_services import JobServices


class JobView(BaseAPIView):
    def __init__(self):
        self.service = JobServices()

    @validate_request(JobFilterSerializer)
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        response, status_code = self.get_response_or_error(service_data)
        return self.response(response, status_code)
    
    @auth_guard(admin=True)
    @validate_request(JobFilterSerializer)
    def post(self, request, data, *args):
        service_data = self.service.post_service(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.response(response, code)