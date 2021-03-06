# Generated by Django 4.0.2 on 2022-03-13 14:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('neighbour', '0002_remove_user_moderation_status_user_bio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('emoji', models.CharField(max_length=10, null=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.CharField(db_index=True, max_length=128, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('title', models.TextField()),
                ('url', models.URLField(max_length=1024, null=True)),
                ('html', models.TextField(null=True)),
                ('comment_count', models.IntegerField(default=0)),
                ('view_count', models.IntegerField(default=0)),
                ('is_commentable', models.BooleanField(default=True)),
                ('is_visible', models.BooleanField(default=False)),
                ('is_pinned_until', models.DateTimeField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='neighbour.user')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='social.category')),
            ],
            options={
                'db_table': 'posts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('html', models.TextField(null=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_pinned', models.BooleanField(default=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='neighbour.user')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='social.post')),
            ],
            options={
                'db_table': 'comments',
                'ordering': ['created_at'],
            },
        ),
    ]
