from datetime import datetime,timedelta
from uuid import uuid4
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    full_name = models.CharField(max_length=128, null=False)
    slug = models.CharField(max_length=32, unique=True)
    address =  models.TextField(blank=True, null=True)

    telegram_id = models.CharField(max_length=128, null=True)
    telegram_data = models.JSONField(null=True)
	
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    last_activity_at = models.DateTimeField(auto_now=True)

    moderation_status = models.BooleanField()

    def __str__(self):
	    return self.slug

    class Meta:
        db_table = "users"
        
    def update_last_activity(self):
        now = datetime.utcnow()
        if self.last_activity_at < now - timedelta(minutes=5):
            return User.objects.filter(id=self.id).update(last_activity_at=now)