from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.api.base_paginated_api import PaginatedBaseApiView
from common.boilerplate.api.custom_pagination import CustomPagination
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from payment.serializers.transaction_serializers import TransactionFilterSerializer, TransactionViewSerializer
from payment.services.transaction_services import TransactionServices


class TransactionViews(BaseAPIView, PaginatedBaseApiView):
    def __init__(self):
        super().__init__(
            serializer_class=TransactionViewSerializer,
            pagination_class=CustomPagination
        )
        self.service = TransactionServices()


    @auth_guard()
    @validate_request(TransactionFilterSerializer)
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        self.queryset, code = self.get_response_or_error(service_data)
        return self.success_paginated(
            page=request.query_params.get("page", 1),
            perPage=request.query_params.get("perPage", 10),
        )