from django.db import models

from common.models.base_model import BaseModel
from property.models.property import Property
from user.models.user import User

class UserPropertyStake(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="stake"
    )
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="property_stakes")
    stake_in_percent = models.FloatField(null=True)