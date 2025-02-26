from rest_framework import serializers

class SingleBlogSerializer(serializers.Serializer):
    blog_id = serializers.UUIDField(required=True)
    title = serializers.CharField(max_length=255, required=False)
    content = serializers.CharField(required=False)
    time_to_read_in_minutes = serializers.IntegerField(required=False)


