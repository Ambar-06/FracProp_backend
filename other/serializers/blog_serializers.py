from rest_framework import serializers

from other.models.blog import Blog

class BlogViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ("meta", "id")


class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)
    content = serializers.CharField(required=True)
    author = serializers.UUIDField(required=True)
    time_to_read_in_minutes = serializers.IntegerField(required=True)