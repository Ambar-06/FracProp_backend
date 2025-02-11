from rest_framework import serializers

from property.models.property_approval_request import PropertyApprovalRequest
from property.serializers.property_serializers import PropertySerializer

class ApprovalRequestViewSerializer(serializers.ModelSerializer):
    property = serializers.SerializerMethodField("get_property")
    requested_by = serializers.SerializerMethodField("get_requested_by")
    
    class Meta:
        model = PropertyApprovalRequest
        exclude = ("created_at", "meta", "id")

    def get_property(self, obj):
        return PropertySerializer(obj.property).data
    
    def get_requested_by(self, obj):
        return {
            "uuid": obj.requested_by.uuid,
            "name": obj.requested_by.first_name + " " + obj.requested_by.last_name,
            "email": obj.requested_by.email,
            "phone_number": obj.requested_by.phone_number,
        }