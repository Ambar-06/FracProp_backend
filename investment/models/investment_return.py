from django.db import models

from common.models.base_model import BaseModel
from property.models.property import Property
from user.models.user import User


class InvestmentReturn(BaseModel):
    """
    This model is used to store the returns of a user for a particular property.
    Creates a new entry in the table whenever a user gets a return from a property.
    """

    RETURN_TYPE_CHOICES = (
        ("RENTAL", "rental"),
        ("VALUATION", "valuation"),
    )

    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="returns"
    )
    property = models.ForeignKey(
        Property,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="property_returns",
    )
    return_in_amount = models.FloatField(null=True)
    return_type = models.CharField(
        max_length=255, null=True, choices=RETURN_TYPE_CHOICES, default="RENTAL"
    )
    return_in_percent = models.FloatField(null=True)
    amount_settled = models.FloatField(null=True)
    credited_to_account = models.BooleanField(default=False)
    amount_credit_date = models.DateTimeField()
