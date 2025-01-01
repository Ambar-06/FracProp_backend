from common.models.base_model import BaseModel
from django.db import models

from property.models.property import Property


class PropertyValuationHistory(BaseModel):
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING, null=True)
    valuation = models.FloatField(null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.property.name