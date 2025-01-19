from django.db import models

from common.models.base_model import BaseModel
from property.models.property import Property
from user.models.user import User

class UserPropertyAmount(BaseModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    total_amount = models.FloatField(null=True)
    total_investment = models.FloatField(null=True)
    total_withdrawal = models.FloatField(null=True)
    total_profit = models.FloatField(null=True)
    total_loss = models.FloatField(null=True)
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="user_property_amounts")