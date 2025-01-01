from django.utils import timezone
from django.db import models
from common.models.base_model import BaseModel
from user.models.user import User


class PasswordManagementUser(BaseModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    unique_token = models.CharField(max_length=255, null=True, unique=True)
    is_used = models.BooleanField(default=False)
    link_generated = models.URLField(max_length=255, null=True, unique=True)
    expiry = models.DateTimeField(null=True)

    @property
    def is_valid(self):
        return self.expiry > timezone.now() and not self.is_used
