from common.boilerplate.api.base_api import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from user.serializers.single_wishlist_serializers import SingleWishlistSerializer
from user.services.single_wishlist_services import SingleWishlistServices


class SingleWishlistView(BaseAPIView):
    def __init__(self):
        self.service = SingleWishlistServices()

    @auth_guard()
    @validate_request(SingleWishlistSerializer)
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        response, status_code = self.get_response_or_error(service_data)
        return self.success(response, status_code)
