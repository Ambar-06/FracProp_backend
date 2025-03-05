from rest_framework import serializers

class SingleRatingAndReviewSerializer(serializers.Serializer):
    rating_id = serializers.UUIDField(required=True)
    rating = serializers.FloatField(required=False)
    review = serializers.CharField(required=False)