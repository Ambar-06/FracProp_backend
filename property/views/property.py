from common.boilerplate.api.base_api import BaseAPIView, BaseModelViewSet
from common.boilerplate.api.base_paginated_api import PaginatedBaseApiView
from common.boilerplate.api.custom_pagination import CustomPagination
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from property.serializers.property_serializers import PropertyFilterSerializer, PropertySerializer
from property.services.property_services import PropertyServices


class PropertyView(BaseAPIView, PaginatedBaseApiView):
    def __init__(self):
        super().__init__(
            serializer_class=PropertySerializer,
            pagination_class=CustomPagination,
        )
        self.service = PropertyServices()

    @auth_guard()
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        self.queryset, status_code = self.get_response_or_error(service_data)
        return self.success_paginated(
            page=request.query_params.get("page", 1), perPage=request.query_params.get("perPage", 10)
        )

    @auth_guard(staff=True)
    @validate_request(PropertyFilterSerializer)
    def post(self, request, data, *args):
        service_data = self.service.post_service(request, data)
        response, status_code = self.get_response_or_error(service_data)
        return self.success(response, status_code)
