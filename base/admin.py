from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Home)