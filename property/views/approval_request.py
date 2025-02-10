from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.api.base_paginated_api import PaginatedBaseApiView
from common.boilerplate.api.custom_pagination import CustomPagination
from common.boilerplate.decorators.auth_guard import auth_guard
from property.serializers.approval_request_serializers import ApprovalRequestViewSerializer
from property.services.approval_request_services import ApprovalRequestServices


class ApprovalRequestView(BaseAPIView, PaginatedBaseApiView):
    def __init__(self):
        super().__init__(
            serializer_class=ApprovalRequestViewSerializer,
            pagination_class=CustomPagination,
        )
        self.service = ApprovalRequestServices()

    @auth_guard(admin=True)
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        self.queryset, code = self.get_response_or_error(service_data)
        return self.success_paginated(
            page=request.query_params.get("page", 1), perPage=request.query_params.get("perPage", 10)
        )
