from django.db import models

from common.models.base_model import BaseModel
from property.models.property import Property
from property.models.property_valuation_history import PropertyValuationHistory


class Survey(BaseModel):

    survey_number = models.BigAutoField()
    surveyor_id = (
        models.UUIDField()
    )  # This id will be unique for each surveyer (a surveryer would be the company employee saved in - internal_frac_prop project)
    surveyor_name = models.CharField(max_length=100, null=True, blank=True)
    surveyor_number = models.CharField(max_length=10, null=True, blank=True)
    surveyor_alt_number = models.CharField(max_length=10, null=True, blank=True)
    surveyor_govt_id_proof = models.ForeignKey()
    surveyor_email = models.EmailField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    property = models.ForeignKey(
        Property, on_delete=models.DO_NOTHING, null=True, related_name="surveys"
    )
    surveyed_valuation = models.ForeignKey(
        PropertyValuationHistory, on_delete=models.DO_NOTHING, null=True
    )

    def __str__(self):
        return self.name
