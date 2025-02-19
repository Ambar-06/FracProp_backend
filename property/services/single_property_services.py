from common.boilerplate.services.base_service import BaseService
from common.helpers.request_validators import PatchRequestValidator
from property.helpers.property import update_property
from property.models.property import Property
from property.serializers.property_serializers import PropertySerializer
from user.models.user import User
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


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
        context = {"request": request}
        return self.ok(PropertySerializer(property, context=context).data)

    def patch_service(self, request, data):
        data = self.validator.validate(data)
        image_urls = []
        user_id = request.user.get("uuid")
        user = self.user_model.objects.filter(uuid=user_id).first()
        uuid = data.get("property_id")
        property = self.model.objects.filter(uuid=uuid).first()
        if not property:
            return self.not_found("Property not found")
        images = request.FILES.getlist("property_images")
        for image in images:
            img_name = image.name.replace(" ", "_")
            path = default_storage.save(f"property_images/{img_name}", ContentFile(image.read()))
            image_urls.append(request.build_absolute_uri(f"/media/{path}"))
        property = update_property(property.uuid, data, image_files=image_urls)
        return self.ok(PropertySerializer(property).data)

    def delete_service(self, request, data):
        property = self.model.objects.filter(uuid=data.get("property_id")).first()
        if not property:
            return self.not_found("Property not found")
        property.is_deleted = True
        property.save()
        return self.ok("Property deleted successfully")
    
    def approve_service(self, request, data):
        property = self.model.objects.filter(uuid=data.get("property_id")).first()
        if not property:
            return self.not_found("Property not found")
        property.is_approved = True
        property.save()
        return self.ok("Property approved successfully")
