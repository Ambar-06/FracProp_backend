from rest_framework import serializers

from property.views.rating_and_review import RatingAndReview

class RatingAndReviewViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingAndReview
        exclude = ("id", "meta")