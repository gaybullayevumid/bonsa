from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs', null=True, blank=True)
    image = models.FileField(upload_to='media/images/') 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title