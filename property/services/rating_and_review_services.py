from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from property.models.property import Property
from property.models.property_average_rating import PropertyAverageRating
from property.models.review_and_rating import ReviewAndRating
from user.models.user import User


class RatingAndReviewServices(BaseService):
    def __init__(self):
        pass

    def get_service(self, request, data):
        user = User.objects.filter(uuid=request.user.get("uuid")).first()
        review_and_rating = ReviewAndRating.objects.filter(user=user)
        return self.ok(review_and_rating, StatusCodes().SUCCESS)

    def post_service(self, request, data):
        user_id = request.user.get("uuid")
        user = User.objects.filter(uuid=user_id).first()
        property = Property.objects.filter(uuid=data.get("property_id")).first()
        ReviewAndRating.objects.create(
            user=user,
            property=property,
            rating=data.get("rating"),
            review=data.get("review")
        )
        ratings = ReviewAndRating.objects.filter(property=property)
        total = 0
        for rating in ratings:
            total += rating.rating
        average_rating = total / ratings.count()
        PropertyAverageRating.objects.create(
            property=property,
            average_rating=average_rating
        )
        return self.ok("Review and rating added successfully", StatusCodes().SUCCESS)