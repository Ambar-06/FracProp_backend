from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from property.models.property_approval_request import PropertyApprovalRequest
from property.serializers.approval_request_serializers import ApprovalRequestViewSerializer
from user.models.user import User



class ApprovalRequestServices(BaseService):
    def __init__(self):
        pass

    def get_service(self, request, data):
        user = User.objects.filter(uuid=request.user.get("uuid")).first()
        if not user.is_admin:
            return self.unauthorized("You are not authorized to view this page")
        request_data = PropertyApprovalRequest.objects.filter(is_approved=False, is_rejected=False)
        return self.ok(ApprovalRequestViewSerializer(request_data, many=True).data, StatusCodes().SUCCESS)