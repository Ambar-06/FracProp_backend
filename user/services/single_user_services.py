from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from user.models.user import User


class SingleUserServices(BaseService):
    def __init__(self):
        self.model = User

    def get_service(self, request, data):
        user = self.model.objects.filter(uuid=data.get("user_id"), is_active=True, is_deleted=False).first()
        if not user:
            return self.not_found("User not found")
        return self.ok(
            {
                "username": user.username,
                "country_code": user.country_code,
                "phone_number": user.phone_number,
                "is_admin": user.is_admin,
                "is_active": user.is_active,
                "last_login": user.last_login,
                "is_phone_verified": user.is_phone_verified,
                "is_email_verified": user.is_email_verified,
            }
        )
    
    def patch_service(self, request, data):
        user_admin = self.model.objects.filter(uuid=request.user.get("uuid"), is_admin=True, is_active=True, is_deleted=False).first()
        if user_admin is None:
            return self.bad_request("You are not authorized to access this resource")
        user = self.model.objects.filter(uuid=data.get("user_id"), is_deleted=False).first()
        if user is None:
            return self.bad_request("User not found")
        user.email = data.get("email") or user.email
        user.is_active = data.get("is_active") or user.is_active
        user.save()
        return self.ok("User updated successfully", StatusCodes().SUCCESS)
    
    def delete_service(self, request, data):
        user_admin = self.model.objects.filter(uuid=request.user.get("uuid"), is_admin=True, is_active=True, is_deleted=False).first()
        if user_admin is None:
            return self.bad_request("You are not authorized to access this resource")
        user = self.model.objects.filter(uuid=data.get("user_id"), is_deleted=False).first()
        if user is None:
            return self.bad_request("User not found")
        user.is_deleted = True
        user.save()
        return self.ok("User deleted successfully", StatusCodes().SUCCESS)