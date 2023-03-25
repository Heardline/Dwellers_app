from django.db import models
from user import User

class Post(models.Model):
    TYPES = {
        'news':'Новость'
    }
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=32, choices=TYPES, default=TYPES['news'], db_index=True)
    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        db_table = 'posts'

    def __str__(self):
        return self.title