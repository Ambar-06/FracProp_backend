from django.db import models

from common.models.base_model import BaseModel
from property.models.property import Property
from user.models.user import User

class UserProperty(BaseModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="user_properties")
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="user_properties")