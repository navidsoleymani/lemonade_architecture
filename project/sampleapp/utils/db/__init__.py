from django.db import models


class BaseManager(models.Manager):
    pass


class Manager(BaseManager.from_queryset(models.QuerySet)):
    pass


class BaseModelClass(models.Model):
    pass
