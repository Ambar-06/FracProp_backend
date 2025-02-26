from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from other.models.blog import Blog
from other.serializers.blog_serializers import BlogViewSerializer


class SingleBlogService(BaseService):
    def __init__(self):
        pass

    def get_service(self, request, data):
        blog_id = data.get("blog_id")
        blog = Blog.objects.filter(uuid=blog_id).first()
        if not blog:
            return self.not_found("Blog not found")
        return self.ok(BlogViewSerializer(blog).data, StatusCodes().SUCCESS)

    def patch_service(self, request, data):
        blog_id = data.get("blog_id")
        blog = Blog.objects.filter(uuid=blog_id).first()
        if not blog:
            return self.not_found("Blog not found")
        blog.title = data.get("title")
        blog.content = data.get("content")
        blog.time_to_read_in_minutes = data.get("time_to_read_in_minutes")
        blog.save()