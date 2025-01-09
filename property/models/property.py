from common.models.base_model import BaseModel
from django.db import models


class Property(BaseModel):
    PROPERTY_TYPE_CHOICES = (
        ("RESIDENTIAL", "residential"),
        ("COMMERCIAL", "commercial"),
        ("INDUSTRIAL", "industrial"),
        ("AGRICULTURAL", "agricultural"),
        ("OTHER", "other"),
    )
    RETURN_TYPE_CHOICES = (
        ("RENT", "rent"),
        ("APPRECIATION", "appreciation"),
        ("OTHER", "other"),
    )

    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(
        max_length=255, null=True, choices=PROPERTY_TYPE_CHOICES, default="RESIDENTIAL"
    )
    number_of_floors = models.IntegerField(null=True, blank=True)
    built_area_in_sqft = models.FloatField(null=True, blank=True)
    area_in_sqft = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    return_type = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices=RETURN_TYPE_CHOICES,
        default="RENT",
    )
    number_of_rooms = models.IntegerField(null=True, blank=True)
    has_loan = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    other_details = models.JSONField(null=True, blank=True)
