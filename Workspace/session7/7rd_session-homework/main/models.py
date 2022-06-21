from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    acti_title = models.CharField(max_length=200)
    acti_date = models.CharField(max_length=100)
    acti_insert = models.TextField()
    acti_image = models.ImageField(upload_to = 'activities/', blank=True, null=True)

    def __str__(self):
        return self.acti_title


class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post ,on_delete=models.CASCADE, related_name ='comments')
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)