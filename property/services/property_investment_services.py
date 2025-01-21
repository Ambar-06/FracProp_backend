from common.boilerplate.services.base_service import BaseService
from property.models.property import Property
from user.models.user import User


class PropertyInvestmentServices(BaseService):
    def __init__(self):
        pass

    def post_service(self, request, data):
        user = User.objects.filter(uuid=request.user.get("uuid")).first()
        property = Property.objects.filter(uuid=data.get("property_id")).first()
        if not property:
            return self.not_found("Property not found")
        amount = data.get("amount")
        
        
        
        