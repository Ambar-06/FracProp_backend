from django.db import models

from common.helpers.constants import EmailTypesDictionary
from common.models.base_model import BaseModel


class EmailTemplate(BaseModel):
    TEMPLATE_TYPE_CHOICES = tuple(
        (k, v.lower()) for k, v in EmailTypesDictionary.items()
    )

    template_type = models.CharField(max_length=255, choices=TEMPLATE_TYPE_CHOICES)
    is_hidden = models.BooleanField(default=False)
    template = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.template_type
