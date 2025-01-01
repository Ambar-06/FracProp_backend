from django.db import models

from common.models.base_model import BaseModel

class Survey(BaseModel):

    survey_number = models.BigIntegerField(null=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name