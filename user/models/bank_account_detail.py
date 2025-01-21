from django.db import models

from common.models.base_model import BaseModel
from user.models.user import User


class BankAccountDetail(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="bank_account_details",
    )
    account_holder_name = models.CharField(max_length=255, null=True, blank=True)
    enctrypted_account_number = models.CharField(max_length=255, null=True, blank=True)
    encrypted_ifsc = models.CharField(max_length=255, null=True, blank=True)
    bank_name = models.CharField(max_length=255, null=True, blank=True)
    branch_name = models.CharField(max_length=255, null=True, blank=True)
    encryption_key_serial = models.IntegerField(null=True, blank=True)
    is_primary = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
