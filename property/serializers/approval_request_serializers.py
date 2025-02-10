from rest_framework import serializers

from property.models.property_approval_request import PropertyApprovalRequest

class ApprovalRequestViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyApprovalRequest
        exclude = ("created_at", "meta", "id")