from common.models.base_model import BaseModel
from django.db import models


class EmailTemplate(BaseModel):
    TEMPLATE_TYPE_CHOICES = (
        ("OTP", "otp"),
        ("RESET_PASSWORD", "reset_password"),
        ("VERIFY_EMAIL", "verify_email"),
    )
    template_type = models.CharField(max_length=255, choices=TEMPLATE_TYPE_CHOICES)
    is_hidden = models.BooleanField(default=False)
    template = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.template_type
