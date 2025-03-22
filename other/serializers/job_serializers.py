from rest_framework import serializers

from other.models.job import Job

class JobFilterSerializer(serializers.Serializer):
    keyword = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    title = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    department = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    location = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    type = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def validate(self, data):
        if self.context.get("request").method == "POST":
            if not data.get("title"):
                raise serializers.ValidationError("Title is required")
            if not data.get("department"):
                raise serializers.ValidationError("Department is required")
            if not data.get("location"):
                raise serializers.ValidationError("Location is required")
            if not data.get("type"):
                raise serializers.ValidationError("Type is required")
            if not data.get("description"):
                raise serializers.ValidationError("Description is required")
        return data

class JobViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        exclude = ("is_deleted", "meta")