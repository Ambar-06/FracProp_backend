from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import DocumentType
from common.helpers.s3_helper import S3BucketHelper
from property.models.property import Property
from property.models.property_approval_request import PropertyApprovalRequest
from property.models.property_data_and_document import PropertyRelatedDataAndDocument
from property.models.property_valuation_history import PropertyValuationHistory
from property.serializers.property_serializers import PropertySerializer
from user.models.user import User
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


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
        image_urls = []
        property = self.model.objects.filter(
            govt_allotted_property_id=data.get("govt_allotted_property_id")
        ).first()
        if property:
            return self.bad_request("Property unique ID already exists")
        user = self.user_model.objects.filter(uuid=request.user.get("uuid")).first()
        images = request.FILES.getlist("property_images")
        for image in images:
            img_name = image.name.replace(" ", "_")
            path = default_storage.save(f"property_images/{img_name}", ContentFile(image.read()))
            image_urls.append(request.build_absolute_uri(f"/media/{path}"))
        print("Got Images")
        print(image_urls)
        data.pop("property_images", None)
        property = self.model.objects.create(**data)
        property_valuation = self.valuation_model.objects.create(
            property=property, valuation=property.valuation
        )
        for url in image_urls:
            PropertyRelatedDataAndDocument.objects.create(document=url, property=property, document_type=DocumentType().PROPERTY_IMAGE)
        PropertyApprovalRequest.objects.create(property=property, requested_by=user)
        return self.ok(PropertySerializer(property, context={"request": request}).data)
