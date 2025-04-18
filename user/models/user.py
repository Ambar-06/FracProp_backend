from django.db import models
from django.db.models import Q

from common.models.base_model import BaseModel


class User(BaseModel):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=14, null=True, blank=True)
    country_code = models.CharField(max_length=5, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    password = models.CharField(max_length=255, null=True, blank=True)
    is_2fa_enabled = models.BooleanField(default=False)
    secret_key = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}-{self.phone_number}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def mobile_number(self):
        return f"{self.country_code}{self.phone_number}"

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=["country_code", "phone_number"],
    #             condition=Q(is_deleted=False),
    #             name="unique_active_user_phone_constraint",
    #         )
    #     ]
    #     unique_together = ("country_code", "phone_number")
