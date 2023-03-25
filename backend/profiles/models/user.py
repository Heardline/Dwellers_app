from django.db import models

from datetime import datetime
from uuid import uuid4


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    full_name = models.CharField(max_length=128, null=False)
    avatar = models.URLField(null=True, blank=True)
    secret_hash = models.CharField(max_length=24, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_activity_at = models.DateTimeField(auto_now=True)

    telegram_id = models.CharField(max_length=128, null=True)
    telegram_data = models.JSONField(null=True)
    is_telegram_verified = models.BooleanField(default=False)

    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)

    is_banned_until = models.DateTimeField(null=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'
        db_table = 'users'

    def __str__(self):
        return f"User: {self.id}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid4()

        if not self.secret_hash:
            self.secret_hash = uuid4().hex

        self.updated_at = datetime.utcnow()
        return super().save(*args, **kwargs)
