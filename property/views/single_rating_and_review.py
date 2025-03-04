from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from property.serializers.rating_and_review_serializers import RatingAndReviewViewSerializer


class SingleRatingAndReviewView(BaseAPIView):
    def __init__(self):
        self.service = ...

    @auth_guard()
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.success(response, code)

    @auth_guard()
    def patch(self, request, data, *args):
        service_data = self.service.patch_service(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.success(response, code)