from rest_framework import serializers

from other.models.blog import Blog

class BlogViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ("meta", "id")