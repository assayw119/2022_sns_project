from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    acti_title = models.CharField(max_length=200)
    acti_date = models.CharField(max_length=100)
    acti_insert = models.TextField()
    acti_image = models.ImageField(upload_to = 'activities/', blank=True, null=True)

    def __str__(self):
        return self.acti_title


