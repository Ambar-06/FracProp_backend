from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from common.models.base_model import BaseModel


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
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    pin_code = models.CharField(max_length=255, null=True, blank=True)
    govt_allotted_property_id = models.CharField(max_length=255, null=True, unique=True)
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
    sold_percentage = models.FloatField(
        null=True,
        blank=True,
        default=0.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
    )
    valuation = models.FloatField(null=True, blank=True)
    investment_lock_in_period_in_months = models.IntegerField(null=True)
    has_loan = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    other_details = models.JSONField(null=True, blank=True)

    class Meta:
        unique_together = ("name", "address", "city", "state", "country", "pin_code")
