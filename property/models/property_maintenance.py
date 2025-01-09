from django.db import models
from common.models.base_model import BaseModel
from property.models.property import Property

class PropertyMaintenance(BaseModel):
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING, null=True, related_name="maintenance")
    maintenance_cost = models.FloatField(null=True, blank=True)
    maintenance_date = models.DateTimeField(null=True, blank=True)
    maintenance_details = models.TextField(null=True, blank=True)
    is_paid = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.property.name} : {self.maintenance_cost} for {self.maintenance_details}"