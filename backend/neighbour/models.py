from datetime import datetime,timedelta
from uuid import uuid4
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    full_name = models.CharField(max_length=62, null=False)
    slug = models.CharField(max_length=32, unique=True)
    address =  models.TextField(blank=True, null=True)
    bio = models.CharField(max_length=128,null=True)
    secret_hash = models.CharField(max_length=24, unique=True)

    telegram_id = models.CharField(max_length=128, null=True)
    telegram_data = models.JSONField(null=True)
	
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    last_activity_at = models.DateTimeField(auto_now=True)
    is_activate = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    is_banned_until = models.DateTimeField(null=True)

    def __str__(self):
	    return self.slug

    class Meta:
        db_table = "users"
        
    def update_last_activity(self):
        now = datetime.utcnow()
        if self.last_activity_at < now - timedelta(minutes=5):
            return User.objects.filter(id=self.id).update(last_activity_at=now)

    @property
    def is_banned(self):
        if self.is_moderator:
            return False
        return self.is_banned_until and self.is_banned_until > datetime.utcnow()