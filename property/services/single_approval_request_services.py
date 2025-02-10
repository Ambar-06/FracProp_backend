from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import ApprovalStatus, StatusCodes
from property.models.property_approval_request import PropertyApprovalRequest
from property.serializers.approval_request_serializers import ApprovalRequestViewSerializer


class SingleApprovalRequestServices(BaseService):
    def __init__(self):
        pass

    def get_service(self, request, data):
        request_id = data.get("request_id")
        request_data = PropertyApprovalRequest.objects.filter(id=request_id).first()
        if not request_data:
            return self.not_found("Approval request not found")
        return self.ok(ApprovalRequestViewSerializer(request_data).data, StatusCodes().SUCCESS)

    def patch_service(self, request, data):
        request_id = data.get("request_id")
        request_data = PropertyApprovalRequest.objects.filter(id=request_id).first()
        if not request_data:
            return self.not_found("Approval request not found")
        if data.get("action") == ApprovalStatus().APPROVED:
            request_data.is_approved = True
        if data.get("action") == ApprovalStatus().REJECTED:
            request_data.is_rejected = True
        request_data.remarks = data.get("remarks")
        request_data.save()