from django.contrib.auth.models import User
from django.db import models
from django.db.models.aggregates import Count
from django.utils.text import slugify
from django.conf import settings

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def post_count(self):
        return self.blogs.count()

    @classmethod
    def get_categories_with_count(cls):
        return cls.objects.annotate(post_count=Count("blogs"))


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="blogs", null=True, blank=True
    )
    image = models.FileField(upload_to="media/images/")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, max_length=255)

    class Meta:
        verbose_name_plural = "Blog"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.post.title}"

    def children(self):
        return self.replies.all().order_by("created_at")

    @property
    def is_parent(self):
        return self.parent is None
