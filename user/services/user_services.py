from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from user.models.user import User


class UserServices(BaseService):
    def __init__(self):
        self.model = User

    def get_service(self, request, data):
        user = self.model.objects.filter(
            uuid=request.user.get("uuid"), is_deleted=False
        ).first()
        if not user.is_admin:
            return self.bad_request("You are not authorized to access this resource")
        users = self.model.objects.all().exclude(is_admin=True)
        return self.ok(users, StatusCodes().SUCCESS)
