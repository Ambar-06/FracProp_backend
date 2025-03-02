from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.api.base_paginated_api import PaginatedBaseApiView
from common.boilerplate.api.custom_pagination import CustomPagination
from common.boilerplate.decorators.auth_guard import auth_guard
from property.serializers.rating_and_review_serializers import RatingAndReviewViewSerializer
from property.services.rating_and_review_services import RatingAndReviewServices


class RatingAndReview(BaseAPIView, PaginatedBaseApiView):
    def __init__(self):
        super().__init__(
            serializer_class=RatingAndReviewViewSerializer,
            pagination_class=CustomPagination,
        )
        self.service = RatingAndReviewServices()

    @auth_guard()
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        self.queryset, code = self.get_response_or_error(service_data)
        self.context = {
            "request": request,
        }
        return self.success_paginated(
            page=request.query_params.get("page", 1),
            perPage=request.query_params.get("perPage", 10),
        )
    
    @auth_guard()
    def post(self, request, data, *args):
        service_data = self.service.post_service(request, data)
        response, code = self.get_response_or_error(service_data)
        return self.success(response, code)
