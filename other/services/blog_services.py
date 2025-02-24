from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from other.models.blog import Blog
from user.models.user import User


class BlogServices(BaseService):
    def __init__(self):
        pass

    def get_service(self, request, data):
        user_id = request.user.get("uuid")
        user = User.objects.filter(uuid=user_id).first()
        return self.ok(Blog.objects.all().order_by("-created_at"), StatusCodes().SUCCESS)

    def post_service(self, request, data):
        pass