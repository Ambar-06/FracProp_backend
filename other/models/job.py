from common.helpers.constants import JobTypesDictionary
from common.models.base_model import BaseModel
from django.db import models

class Job(BaseModel):
    JOB_TYPE_CHOICES = tuple(
        (k, v.lower()) for k, v in JobTypesDictionary.items()
    )

    title = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, choices=JOB_TYPE_CHOICES)
    posted = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)