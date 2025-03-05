from common.models.base_model import BaseModel
from django.db import models

from user.models.user import User


class Blog(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="blogs")
    time_to_read_in_minutes = models.IntegerField(default=0)