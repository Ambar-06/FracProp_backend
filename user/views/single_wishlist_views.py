from common.boilerplate.api.base_api import BaseAPIView
from user.services.single_wishlist_services import SingleWishlistServices


class SingleWishlistViews(BaseAPIView):
    def __init__(self):
        self.service = SingleWishlistServices()

    def get(self, request, data, *args):
        pass

    def patch(self, request, data, *args):
        pass