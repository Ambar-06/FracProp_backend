from django.db import models

from common.models.base_model import BaseModel
from user.models.user import User


class Investment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    amount = models.FloatField(null=True)

    def __str__(self):
        return "self.name"
