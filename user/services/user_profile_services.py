from common.boilerplate.services.base_service import BaseService
from user.models.user import User
from user.serializers.user_serializers import UserViewSerializer


class UserProfileService(BaseService):
    def __init__(self):
        pass

    def get_service(self, request, data):
        user = User.objects.filter(uuid=request.user.get("uuid")).first()
        if not user:
            return self.not_found("User not found")
        return self.ok(UserViewSerializer(user).data)
    
    def patch_service(self, request, data):
        user = User.objects.filter(uuid=request.user.get("uuid")).first()
        if not user:
            return self.not_found("User not found")
        user.first_name = data.get("first_name") or user.first_name
        user.last_name = data.get("last_name") or user.last_name
        user.email = data.get("email") or user.email
        user.phone_number = data.get("phone_number") or user.phone_number
        user.country_code = data.get("country_code") or user.country_code
        user.save()
        return self.ok("User updated successfully")