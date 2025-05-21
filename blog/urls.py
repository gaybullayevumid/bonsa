from django.urls import path
from .views import *

urlpatterns = [
    path("blog/", BlogListView.as_view(), name="blog"),
    path("blog-details/<slug:slug>/", BlogDetailView.as_view(), name="blog_details"),
]
