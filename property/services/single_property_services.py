from common.boilerplate.services.base_service import BaseService
from common.helpers.request_validators import PatchRequestValidator
from property.helpers.property import update_property
from property.models.property import Property
from property.serializers.property_serializers import PropertySerializer
from user.models.user import User


class SinglePropertyServices(BaseService):
    def __init__(self):
        self.model = Property
        self.user_model = User
        self.validator = PatchRequestValidator()

    def get_service(self, request, data):
        uuid = data.get("property_id")
        property = self.model.objects.filter(uuid=uuid).first()
        if not property:
            return self.not_found("Property not found")
        return self.ok(PropertySerializer(property).data)
        

    def patch_service(self, request, data):
        data = self.validator.validate(data)
        user_id = request.user.get("uuid")
        user = self.user_model.objects.filter(uuid=user_id).first()
        uuid = data.get("property_id")
        property = self.model.objects.filter(uuid=uuid).first()
        if not property:
            return self.not_found("Property not found")
        property = update_property(property.uuid, data)
        return self.ok(PropertySerializer(property).data)
        

    def delete_service(self, request, data):
        pass