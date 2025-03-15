from django.db import models

from common.helpers.constants import DocumentTypesDictionary
from common.models.base_model import BaseModel
from property.models.property import Property


class PropertyRelatedDataAndDocument(BaseModel):
    DOCUMENT_TYPE_CHOICES = tuple(
        (k, v.lower()) for k, v in DocumentTypesDictionary.items()
    )

    property = models.ForeignKey(
        Property,
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="property_documents",
    )
    document_type = models.CharField(
        max_length=255, null=True, choices=DOCUMENT_TYPE_CHOICES
    )
    document_date = models.DateField(null=True)
    document_expiry_date = models.DateField(null=True)
    document = models.URLField(null=True)

    def __str__(self):
        return self.property.name
