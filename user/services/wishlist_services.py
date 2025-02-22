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
        wishlist = user.wishlist.filter(is_active=True).value_list(
            "property_id", flat=True
        )
        properties = Property.objects.filter(uuid__in=wishlist)
        return self.ok(properties, StatusCodes().SUCCESS)

    def post_service(self, request, data):
        user_id = request.user.get("uuid")
        user = User.objects.filter(uuid=user_id).first()
        property_id = data.get("property_id")
        property = Property.objects.filter(uuid=property_id).first()
        wishlist_obj = Wishlist.objects.filter(user=user, property=property).first()
        if wishlist_obj:
            if wishlist_obj.is_active:
                wishlist_obj.is_active = False
                wishlist_obj.save()
                return self.ok("Property removed from wishlist", StatusCodes().SUCCESS)
            else:
                wishlist_obj.is_active = True
                wishlist_obj.save()
                return self.ok("Property added to wishlist", StatusCodes().SUCCESS)
        Wishlist.objects.create(user=user, property=property)
        return self.ok("Property added to wishlist", StatusCodes().SUCCESS)
