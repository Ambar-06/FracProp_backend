from common.boilerplate.services.base_service import BaseService
from common.helpers.s3_helper import S3BucketHelper
from property.models.property import Property
from property.serializers.property_serializers import PropertySerializer
from user.models.user import User


class PropertyServices(BaseService):
    def __init__(self):
        self.model = Property
        self.s3_helper = S3BucketHelper()
        self.user_model = User

    def get_service(self, request, data):
        user_id = request.user.get("uuid")
        user = self.user_model.objects.filter(uuid=user_id).first()
        if not user:
            return self.not_found("User not found")
        properties = self.model.objects.all()
        if not user.is_admin:
            properties = properties.filter(is_active=True)
        return self.ok(PropertySerializer(properties, many=True).data)