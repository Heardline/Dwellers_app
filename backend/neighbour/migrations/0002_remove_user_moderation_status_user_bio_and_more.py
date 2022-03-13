# Generated by Django 4.0.2 on 2022-03-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='moderation_status',
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_activate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_banned_until',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_moderator',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=62),
        ),
    ]