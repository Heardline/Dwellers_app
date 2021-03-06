import datetime
import random
import string
from uuid import uuid4
from django.db import models
from neighbour.models import User
# Create your models here.

class Session(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, related_name="sessions", db_index=True, on_delete=models.CASCADE)

    token = models.CharField(max_length=128, unique=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "sessions"

class Code(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    recipient = models.CharField(max_length=128, db_index=True)
    code = models.CharField(max_length=128, db_index=True)

    user = models.ForeignKey(User, related_name="codes", db_index=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True)

    attempts = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "codes"
        ordering = ["-created_at"]

    @classmethod
    def create_for_user(cls, user: User, recipient: str, length=6):
        recipient = recipient.lower()
        last_codes_count = Code.objects.filter(
            recipient=recipient,
            created_at__gte=datetime.utcnow() - datetime.timedelta(hours=2),
        ).count()
        if last_codes_count >= 5:
            raise "Слишком много раз вы запросили код. Если что-то не получается, напишите главному"

        return Code.objects.create(
            recipient=recipient,
            user=user,
            code= "".join(random.choice(string.digits) for i in range(length)),
            created_at=datetime.utcnow(),
            expires_at=datetime.utcnow() + datetime.timedelta(minutes=20),
        )

    @classmethod
    def check_code(cls, recipient: str, code: str) -> User:
        recipient = recipient.lower()
        last_code = Code.objects.filter(recipient=recipient).order_by("-created_at").first()
        if not last_code:
            raise "Код не верный"

        if last_code.attempts >= 3:
            raise "Вы ввели код неправильно несколько раз. Придётся запросить его заново"

        if last_code.is_expired() or last_code.code != code:
            last_code.attempts += 1
            last_code.save()
            raise "Код не верный"

        Code.objects.filter(recipient=recipient).delete()
        return last_code.user

    def is_expired(self):
        return self.expires_at <= datetime.utcnow()