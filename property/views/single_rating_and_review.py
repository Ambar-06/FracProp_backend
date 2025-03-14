from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from property.serializers.single_rating_and_review_serializers import SingleRatingAndReviewSerializer
from property.services.single_rating_and_review_services import SingleRatingAndReviewServices


class SingleRatingAndReviewView(BaseAPIView):
    def __init__(self):
        self.service = SingleRatingAndReviewServices()

    @auth_guard()
    @validate_request(SingleRatingAndReviewSerializer)
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.response(response, code)

    @auth_guard()
    @validate_request(SingleRatingAndReviewSerializer)
    def patch(self, request, data, *args):
        service_data = self.service.patch_service(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.response(response, code)
    
    @auth_guard()
    @validate_request(SingleRatingAndReviewSerializer)
    def delete(self, request, data, *args):
        service_data = self.service.delete_service(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.response(response, code)