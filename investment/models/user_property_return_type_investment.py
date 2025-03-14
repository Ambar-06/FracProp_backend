from common.models.base_model import BaseModel
from django.db import models

from user.models.user import User


class UserPropertyReturnTypeInvestment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    amount = models.FloatField(null=True)
    property_return_type = models.CharField(max_length=255, null=True, blank=True)
