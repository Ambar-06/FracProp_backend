from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from notification.models.email_template import EmailTemplate
from notification.serializers.template_serializers import TemplateViewSerializer


class TemplateServices(BaseService):
    def __init__(self):
        pass

    def get_service(self, request, data):
        templates = EmailTemplate.objects.all()
        return self.ok(templates, StatusCodes().SUCCESS)

    def post_service(self, request, data):
        if EmailTemplate.objects.filter(template_type=data.get("template_type")).exists():
            return self.exception(f"Template with type {data.get("template_type")} already exists", StatusCodes().UNPROCESSABLE_ENTITY)
        template = EmailTemplate.objects.create(
            template=data.get("template"), template_type=data.get("template_type"), is_hidden=data.get("is_hidden")
        )
        return self.ok(TemplateViewSerializer(template).data, StatusCodes().CREATED)