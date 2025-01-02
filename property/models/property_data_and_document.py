from common.models.base_model import BaseModel
from django.db import models

from property.models.property import Property


class PropertyDataAndDocument(BaseModel):
    DOCUMENT_TYPE_CHOICES = (
        ("PROPERTY_PAPER", "property_paper"),
        ("PROPERTY_IMAGE", "property_image"),
        ("PROPERTY_VIDEO", "property_video"),
        ("LOAN_DOCUMENT", "loan_document"),
        ("OTHER_DOCUMENT", "other_document"),
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
    document = models.URLField(null=True)

    def __str__(self):
        return self.property.name
