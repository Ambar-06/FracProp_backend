from django.db import models
import uuid


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return (
            super(BaseModelManager, self)
            .get_queryset()
            .filter(is_deleted__in=[False, None])
        )


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    meta = models.JSONField(null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True)
    is_deleted = models.BooleanField(default=False, db_index=True)
    objects = BaseModelManager()

    class Meta:
        get_latest_by = "updated_at"
        abstract = True


class TimeStampedModelManager(models.Manager):
    def get_queryset(self):
        return (
            super(TimeStampedModelManager, self).get_queryset().filter(is_deleted=False)
        )


class TimeStampedModel(models.Model):
    """TimeStampedModel
     An abstract base class model that provides self-managed "created" and
    "modified" fields.
    """

    created_on = models.DateTimeField(auto_now_add=True, db_column="created_on")
    updated_on = models.DateTimeField(auto_now=True, db_column="updated_on")
    is_deleted = models.BooleanField(default=False)

    objects = TimeStampedModelManager()

    class Meta:
        get_latest_by = "updated_on"
        abstract = True
        default_permissions = ()
