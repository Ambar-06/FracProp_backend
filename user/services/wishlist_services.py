from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from property.models.property import Property
from user.models.user import User
from user.models.wishlist import Wishlist


class WishlistServices(BaseService):
    def __init__(self):
        pass

    def get_service(self, request, data):
        user_id = request.user.get("uuid")
        user = User.objects.filter(uuid=user_id).first()
        wishlist = user.wishlist.all().value_list("property_id", flat=True)
        properties = Property.objects.filter(uuid__in=wishlist)
        return self.ok(properties, StatusCodes().SUCCESS)

    def post_service(self, request, data):
        user_id = request.user.get("uuid")
        user = User.objects.filter(uuid=user_id).first()
        property_id = data.get("property_id")
        property = Property.objects.filter(uuid=property_id).first()
        wishlist_qs = Wishlist.objects.filter(user=user, property=property)
        if len(wishlist_qs.filter(is_active=True)) > 0:
            return self.ok("Property already in wishlist", StatusCodes().SUCCESS)
        if wishlist_qs.first():
            wishlist_qs.update(is_active=True)
            return self.ok("Property added to wishlist", StatusCodes().SUCCESS)
        Wishlist.objects.create(user=user, property=property)
        return self.ok("Property added to wishlist", StatusCodes().SUCCESS)
        