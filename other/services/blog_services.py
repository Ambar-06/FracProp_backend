from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from other.models.blog import Blog
from other.serializers.blog_serializers import BlogViewSerializer
from user.models.user import User


class BlogServices(BaseService):
    def __init__(self):
        pass

    def get_service(self, request, data):
        user_id = request.user.get("uuid")
        user = User.objects.filter(uuid=user_id).first()
        return self.ok(Blog.objects.all().order_by("-created_at"), StatusCodes().SUCCESS)

    def post_service(self, request, data):
        user_id = request.user.get("uuid")
        user = User.objects.filter(uuid=user_id).first()
        data["author"] = user
        blog = Blog.objects.create(**data)
        return self.ok(BlogViewSerializer(blog).data, StatusCodes().CREATED)