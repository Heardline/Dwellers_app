from django.db import models

# Create your models here.
class Message(models.Model):
    message_id = models.CharField(max_length=128, null=True)
    message_text = models.TextField(null=True)
    from_id = models.CharField(max_length=128, null=True)

    created_at = created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.created_at} from {self.from_id}"
    class Meta:
        db_table = "message_telegram"