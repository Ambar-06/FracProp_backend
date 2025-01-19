from django.db import models

from common.models.base_model import BaseModel
from user.models.user import User

class Transaction(BaseModel):
    TRANSACTION_TYPE_CHOICES = (
        ("DEPOSIT", "deposit"),
        ("WITHDRAWAL", "withdrawal"),
    )

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    amount = models.FloatField(null=True)
    type = models.CharField(
        max_length=255, null=True, choices=TRANSACTION_TYPE_CHOICES, default="DEPOSIT"
    )
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.type} : {self.amount}"