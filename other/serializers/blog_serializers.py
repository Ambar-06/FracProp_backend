from rest_framework import serializers
from other.helpers.blog_helper import remove_html_tags
from other.models.blog import Blog

class BlogViewSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField("get_content")
    class Meta:
        model = Blog
        exclude = ("meta", "id")

    def get_content(self, obj):
        list_view = self.context.get("list_view")
        if list_view:
            content = remove_html_tags(obj.content)
            return content
        return obj.content
    


class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)
    content = serializers.CharField(required=True)
    author = serializers.UUIDField(required=True)
    time_to_read_in_minutes = serializers.IntegerField(required=True)