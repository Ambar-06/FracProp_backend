from django.db import models

from common.models.base_model import BaseModel
from property.models.property import Property


class PropertyValuationHistory(BaseModel):
    property = models.ForeignKey(
        Property,
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="valuation_history",
    )
    valuation = models.FloatField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.property.name
