from django.db import models

from common.models.base_model import BaseModel
from property.models.property import Property
from property.models.property_data_and_document import PropertyDataAndDocument

class PropertyRentalData(BaseModel):
    RENTAL_AREA_TYPE = (
        ("ROOM", "room"),
        ("FLAT", "flat"),
        ("HOUSE", "house"),
        ("OTHER", "other"), 
        ("COMMERCIAL", "commercial"),  
    )

    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="rental_data")
    rental_area_type = models.CharField(max_length=255, null=True, blank=True, choices=RENTAL_AREA_TYPE, default="ROOM")
    house_number = models.CharField(max_length=255, null=True, blank=True)
    floor_number = models.IntegerField(null=True, blank=True)
    room_number = models.IntegerField(null=True, blank=True)
    rent_per_month = models.FloatField(null=True, blank=True)
    security_deposit = models.FloatField(null=True, blank=True)
    agreement = models.ForeignKey(PropertyDataAndDocument, on_delete=models.DO_NOTHING, null=True, blank=True)