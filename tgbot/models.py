from uuid import uuid4
from django.db import models


class CreateTracker(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    class Meta:
        abstract = True
        ordering = ('-created_at',)

class CreateUpdateTracker(CreateTracker):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(CreateTracker.Meta):
        abstract = True
class User(CreateUpdateTracker):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    telegram_id = models.IntegerField()
    full_name = models.CharField(max_length=120)

    is_blocked_bot = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)
