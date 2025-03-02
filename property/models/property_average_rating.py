from common.models.base_model import BaseModel
from django.db import models

from property.models.property import Property


class PropertyAverageRating(BaseModel):
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING, null=True, related_name='property_average_rating')
    average_rating = models.FloatField(null=True)