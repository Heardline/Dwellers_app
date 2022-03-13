import datetime,slugify
from enum import unique
from uuid import uuid4
from django.db import models
from django.db.models import F
from neighbour.models import User


# Модель для поста

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=64,null=False)
    emoji = models.CharField(max_length=10,null=True)

    class Meta:
        db_table = 'categories'

class Post(models.Model):

    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    slug = models.CharField(max_length=128,unique=True,db_index=True)

    author = models.ForeignKey(User,related_name="posts",on_delete=models.CASCADE)
    type = models.ForeignKey(Category,related_name="category",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,db_index=True)

    title = models.TextField(null=False)
    url = models.URLField(max_length=1024,null=True)
    html = models.TextField(null=True)

    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    is_commentable = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=False)
    is_pinned_until = models.DateTimeField(null=True)
    
    class Meta:
        db_table = "posts"
        ordering = ["-created_at"]
    
    def to_dict(self):
        return {
            "id":str(self.id),
            "type":self.type,
            "slug":self.slug,
            "title": self.title,
            "html": self.html,
            "created_at":self.created_at,
            "view_count":self.view_count,
        }
    
    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title[:20],separator="-")
        return super().save(*args, **kwargs)
    
    def increment_view_count(self):
        return Post.objects.filter(id=self.id).update(view_count=F("view_count") + 1)

    def can_edit(self, user):
        return self.author == user or user.is_moderator
    
    def delete(self, *args, **kwargs):
        self.is_visible = False
        self.save()


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    author = models.ForeignKey(User, related_name="comments", null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    html = models.TextField(null=True)

    is_visible = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)

    class Meta:
        db_table = "comments"
        ordering = ["created_at"]
    
    def to_dict(self):
        return {
            "id": str(self.id),
            "author": self.author,
        }

    def delete(self):
        self.is_deleted = True
        self.save()