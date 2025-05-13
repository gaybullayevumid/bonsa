from .models import *
from django.views.generic import ListView, DetailView

# Create your views here.

class BlogListView(ListView):
    model = Blog
    template_name = 'pages/blog.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(
            post_count=Count('blogs')
        )
        return context

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'pages/blog-details.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object

        context['categories'] = Category.objects.annotate(
            post_count=Count('blogs')
        )
        context['last_posts'] = Blog.objects.order_by('-created_at')
        context["prev_post"] = Blog.objects.filter(
            created_at__lt=post.created_at
        ).order_by('-created_at').first()
        context["next_post"] = Blog.objects.filter(
            created_at__gt=post.created_at
        ).order_by('created_at').first()
        return context

