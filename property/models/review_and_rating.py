from django.db import models

from common.models.base_model import BaseModel
from property.models.property import Property
from user.models.user import User

class ReviewAndRating(BaseModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name='user_review')
    review = models.TextField(null=True)
    rating = models.FloatField(null=True)
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING, null=True, related_name='property_review')