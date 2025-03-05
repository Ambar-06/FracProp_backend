from rest_framework import serializers

from property.models.review_and_rating import ReviewAndRating


class RatingAndReviewViewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField("get_user")

    class Meta:
        model = ReviewAndRating
        exclude = ("id", "meta")

    def get_user(self, obj):
        return {
            "uuid": obj.user.uuid,
            "name": obj.user.full_name,
            "email": obj.user.email,
            "phone_number": obj.user.mobile_number,
        }


class RatingAndReviewFilterSerializer(serializers.Serializer):
    rating = serializers.IntegerField(required=False, min_value=1, max_value=5)
    review = serializers.CharField(required=False, max_length=500)
    property_id = serializers.UUIDField(required=False)

    def validate(self, attrs):
        if self.context.get("request").method == "POST":
            if not attrs.get("property_id"):
                raise serializers.ValidationError("Property id is required")
            if not attrs.get("rating") or not attrs.get("review"):
                raise serializers.ValidationError("Rating or review is required")
        return attrs