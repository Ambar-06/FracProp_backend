from django.db import models

from common.models.base_model import BaseModel
from investment.models.investment import Investment
from user.models.user import User

class InvestmentReturn(BaseModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='returns')
    investment = models.ForeignKey(Investment, on_delete=models.DO_NOTHING, null=True, blank=True)
    return_in_amount = models.FloatField(null=True)
    return_in_percent = models.FloatField(null=True)
    credited_to_account = models.BooleanField(default=False)
    