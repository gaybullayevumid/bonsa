# Generated by Django 5.1.6 on 2025-02-20 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_blog_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_1', models.CharField(max_length=255)),
                ('title_2', models.CharField(max_length=255)),
                ('about', models.TextField()),
            ],
        ),
    ]
