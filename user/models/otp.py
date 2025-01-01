from django.db import models
from django.utils import timezone
from common.models.base_model import BaseModel
from user.models.user import User


class OTP(BaseModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="otps")
    otp = models.CharField(max_length=6)
    is_used = models.BooleanField(default=False)
    expiry = models.DateTimeField()

    def __str__(self):
        return self.otp

    def save(self, *args, **kwargs):
        self.expiry = timezone.now() + timezone.timedelta(minutes=10)
        super().save(*args, **kwargs)

    @property
    def is_valid(self):
        return self.expiry > timezone.now()
