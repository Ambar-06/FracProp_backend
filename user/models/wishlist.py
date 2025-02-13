from common.models.base_model import BaseModel
from django.db import models

from user.models.user import User
from property.models import Property

class Wishlist(BaseModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='wishlist')
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING, related_name='wishlist')
    is_active = models.BooleanField(default=True)