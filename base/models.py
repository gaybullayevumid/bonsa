from django.db import models

# Create your models here.


class Home(models.Model):
    title_1 = models.CharField(max_length=255)
    title_2 = models.CharField(max_length=255)
    about = models.TextField()

    class Meta:
        verbose_name_plural = "Home"


class About(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "About"


class ContactInfo(models.Model):
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    email1 = models.EmailField()
    email2 = models.EmailField()
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)

    def __str__(self):
        return self.email1