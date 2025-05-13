from django.db import models
from django.db.models.aggregates import Count
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def post_count(self):
        return self.blogs.count()

    @classmethod
    def get_categories_with_count(cls):
        return cls.objects.annotate(post_count=Count('blogs'))

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs', null=True, blank=True)
    image = models.FileField(upload_to='media/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, max_length=255)

    class Meta:
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)