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
        rating = self.model.objects.filter(uuid=rating_id).first()
        if not rating:
            return self.not_found("Rating not found")
        if not user.is_admin:
            if rating.user != user:
                return self.forbidden("You are not authorized to view this rating")
        return self.ok(RatingAndReviewViewSerializer(rating).data, StatusCodes().SUCCESS)


    def patch_service(self, request, data):
        rating_id = data.get("rating_id")
        user_id = request.user.get("uuid")
        user = User.objects.filter(uuid=user_id).first()
        rating = self.model.objects.filter(uuid=rating_id).first()
        if not rating:
            return self.not_found("Rating not found")
        if not user.is_admin:
            if rating.user != user:
                return self.forbidden("You are not authorized to update this rating")
        rating.rating = data.get("rating", rating.rating)
        rating.review = data.get("review", rating.review)
        rating.save()
        return self.ok(RatingAndReviewViewSerializer(rating).data, StatusCodes().SUCCESS)
    
    def delete_service(self, request, data):
        rating_id = data.get("rating_id")
        user_id = request.user.get("uuid")
        user = User.objects.filter(uuid=user_id).first()
        rating = self.model.objects.filter(uuid=rating_id).first()
        if not rating:
            return self.not_found("Rating not found")
        if not user.is_admin:
            if rating.user != user:
                return self.forbidden("You are not authorized to delete this rating")
        rating.is_deleted = True
        rating.save()
        return self.ok("Rating deleted successfully", StatusCodes().SUCCESS)