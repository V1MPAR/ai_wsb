import uuid

from django.db import models


# Create your models here.
class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=64, unique=True)
