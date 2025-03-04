from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from property.models.review_and_rating import ReviewAndRating
from property.serializers.rating_and_review_serializers import RatingAndReviewViewSerializer
from user.models.user import User


class SingleRatingAndReviewServices(BaseService):
    def __init__(self):
        self.model = ReviewAndRating

    def get_service(self, request, data):
        rating_id = data.get("rating_id")
        user_id = request.user.get("uuid")
        user = User.objects.filter(uuid=user_id).first()
        rating = self.model.objects.filter(uuid=rating_id, user=user).first()
        if not rating:
            return self.not_found("Rating not found")
        return self.ok(RatingAndReviewViewSerializer(rating).data, StatusCodes().SUCCESS)


    def patch_service(self, request, data):
        pass