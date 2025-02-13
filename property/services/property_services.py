from common.boilerplate.services.base_service import BaseService
from common.helpers.s3_helper import S3BucketHelper
from property.models.property import Property
from property.models.property_approval_request import PropertyApprovalRequest
from property.models.property_valuation_history import PropertyValuationHistory
from property.serializers.property_serializers import PropertySerializer
from user.models.user import User


class PropertyServices(BaseService):
    def __init__(self):
        self.model = Property
        self.s3_helper = S3BucketHelper()
        self.user_model = User
        self.valuation_model = PropertyValuationHistory

    def get_service(self, request, data):
        user_id = request.user.get("uuid")
        user = self.user_model.objects.filter(uuid=user_id).first()
        properties = self.model.objects.filter(is_approved=True)
        if not user.is_admin:
            properties = properties.filter(is_active=True)
        return self.ok(properties)

    def post_service(self, request, data):
        property = self.model.objects.filter(
            govt_allotted_property_id=data.get("govt_allotted_property_id")
        ).first()
        if property:
            return self.bad_request("Property unique ID already exists")
        user = self.user_model.objects.filter(uuid=request.user.get("uuid")).first()
        property = self.model.objects.create(**data)
        property_valuation = self.valuation_model.objects.create(
            property=property, valuation=property.valuation
        )
        PropertyApprovalRequest.objects.create(property=property, requested_by=user)
        return self.ok(PropertySerializer(property, context={"request": request}).data)
