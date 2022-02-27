from django.contrib import admin
from .models import User

class UsersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'address', 'telegram_id', 'moderation_status')

# Register your models here.

admin.site.register(User, UsersAdmin)
# Register your models here.
