from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from other.models.blog import Blog
from other.serializers.blog_serializers import BlogViewSerializer
from user.models.user import User


class OpenBlogServices(BaseService):
    def __init__(self):
        pass

    def get_service(self, request):
        return self.ok(Blog.objects.all().order_by("-created_at"), StatusCodes().SUCCESS)