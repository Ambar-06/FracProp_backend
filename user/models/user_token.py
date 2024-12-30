from django.db import models
from user.models.user import User
from common.models.base_model import BaseModel
from django.utils import timezone

class UserToken(BaseModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='token')
    token = models.CharField(max_length=500)
    expiry = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
    
    @property
    def is_valid(self):
        return self.expiry > timezone.now() and self.is_active