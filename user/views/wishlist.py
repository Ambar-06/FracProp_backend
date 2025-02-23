from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.api.base_paginated_api import PaginatedBaseApiView
from common.boilerplate.api.custom_pagination import CustomPagination
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from property.serializers.property_serializers import PropertySerializer
from user.serializers.wishlist_serializers import WishlistSerializer
from user.services.wishlist_services import WishlistServices


class WishlistView(BaseAPIView, PaginatedBaseApiView):
    def __init__(self):
        super().__init__(
            serializer_class=PropertySerializer,
            pagination_class=CustomPagination,
        )
        self.service = WishlistServices()

    @auth_guard()
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        self.queryset, status_code = self.get_response_or_error(service_data)
        self.context = {"request": request}
        return self.success_paginated(
            page=request.query_params.get("page", 1),
            perPage=request.query_params.get("perPage", 10),
        )

    @auth_guard()
    @validate_request(WishlistSerializer)
    def post(self, request, data, *args):
        service_data = self.service.post_service(request, data)
        response, status_code = self.get_response_or_error(service_data)
        return self.success(response, status_code)
