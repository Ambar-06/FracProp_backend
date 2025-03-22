from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.api.base_paginated_api import PaginatedBaseApiView
from common.boilerplate.api.custom_pagination import CustomPagination
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from other.serializers.blog_serializers import BlogViewSerializer
from other.services.open_blog_services import OpenBlogServices


class OpenBlogView(BaseAPIView, PaginatedBaseApiView):
    def __init__(self):
        super().__init__(
            serializer_class=BlogViewSerializer,
            pagination_class=CustomPagination,
        )
        self.service = OpenBlogServices()

    def get(self, request, *args):
        service_data = self.service.get_service(request)
        self.queryset, status_code = self.get_response_or_error(service_data)
        self.context = {
            "request": request,
            "list_view" :True,
        }
        return self.success_paginated(
            page=request.query_params.get("page", 1),
            perPage=request.query_params.get("perPage", 10),
        )

