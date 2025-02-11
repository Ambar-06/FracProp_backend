from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import ApprovalStatus, StatusCodes
from property.models.property import Property
from property.models.property_approval_request import PropertyApprovalRequest
from property.models.property_valuation_history import PropertyValuationHistory
from property.serializers.approval_request_serializers import ApprovalRequestViewSerializer


class SingleApprovalRequestServices(BaseService):
    def __init__(self):
        pass

    def get_service(self, request, data):
        request_id = data.get("request_id")
        request_data = PropertyApprovalRequest.objects.filter(uuid=request_id).first()
        if not request_data:
            return self.not_found("Approval request not found")
        return self.ok(ApprovalRequestViewSerializer(request_data).data, StatusCodes().SUCCESS)

    def patch_service(self, request, data):
        request_id = data.get("request_id")
        request_data = PropertyApprovalRequest.objects.filter(uuid=request_id).first()
        if not request_data:
            return self.not_found("Approval request not found")
        property = request_data.property
        if data.get("action") == ApprovalStatus().APPROVE:
            request_data.is_approved = True
            property.is_approved = True
            property.save()
        if data.get("action") == ApprovalStatus().REJECT:
            request_data.is_rejected = True
        request_data.remarks = data.get("remarks")
        request_data.save()