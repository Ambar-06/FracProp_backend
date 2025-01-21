from django.db import models

from common.models.base_model import BaseModel
from property.models.property import Property
from user.models.user import User


class Investment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    amount = models.FloatField(null=True)
    property = models.ForeignKey(
        Property,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="investments",
    )

    def __str__(self):
        return f"{self.user.name} : {self.amount}"
