from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from property.serializers.property_serializers import PropertySerializer
from user.models.wishlist import Wishlist


class SingleWishlistServices(BaseService):
    def __init__(self):
        pass

    def get_service(self, request, data):
        wishlist_id = data.get("wishlist_id")
        wishlist = Wishlist.objects.filter(
            uuid=wishlist_id, user__uuid=request.user.get("uuid")
        ).first()
        if not wishlist:
            return self.ok("Wishlisted Property not found", StatusCodes().NOT_FOUND)
        return self.ok(
            PropertySerializer(wishlist.property).data, StatusCodes().SUCCESS
        )
