from uuid import uuid4
from django.db import models
# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    telegram_id = models.IntegerField()
    full_name = models.CharField(max_lenght=128)