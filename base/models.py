from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    type = models.CharField(max_length=255)
    image = models.FileField(upload_to='media/images/') 
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title