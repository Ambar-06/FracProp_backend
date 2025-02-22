from common.models.base_model import BaseModel
from django.db import models

from property.models.property import Property
from user.models.user import User


class PropertyApprovalRequest(BaseModel):
    property = models.ForeignKey(
        Property,
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="approval_requests",
    )
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    reason = models.TextField(null=True)
    requested_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="approval_requests_requested",
    )
    approved_rejected_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="approval_requests_approved_rejected",
    )
    approved_rejected_on = models.DateTimeField(null=True)
