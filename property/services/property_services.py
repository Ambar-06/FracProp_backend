from common.boilerplate.services.base_service import BaseService
from property.models.property import Property


class PropertyServices(BaseService):
    def __init__(self):
        self.model = Property

    def create_property(self, data):
        return self.model.objects.create(**data)

    def create_property_document(self, data):
        ...