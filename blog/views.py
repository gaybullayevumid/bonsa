from django.shortcuts import redirect
from pyexpat.errors import messages

from .forms import CommentForm
from .models import *
from django.views.generic import ListView, DetailView

# Create your views here.


class BlogListView(ListView):
    model = Blog
    template_name = "pages/posts/blog.html"
    context_object_name = "posts"
    ordering = ["-created_at"]
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.annotate(post_count=Count("blogs"))
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = "pages/posts/blog-details.html"
    context_object_name = "post"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object

        context["categories"] = Category.objects.annotate(post_count=Count("blogs"))
        context["last_posts"] = Blog.objects.order_by("-created_at")
        context["prev_post"] = (
            Blog.objects.filter(created_at__lt=post.created_at)
            .order_by("-created_at")
            .first()
        )
        context["next_post"] = (
            Blog.objects.filter(created_at__gt=post.created_at)
            .order_by("created_at")
            .first()
        )

        context["form"] = CommentForm()
        context["comments"] = post.comments.order_by("-created_at")

        reply_to = self.request.GET.get('reply')
        if reply_to:
            try:
                context['reply_to'] = int(reply_to)
            except ValueError:
                context['reply_to'] = None
        else:
            context['reply_to'] = None
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
            messages.error(request, "Kamentariya yozish uchun oldin login qiling!")
            return redirect("login")

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("blog_details", slug=self.object.slug)
        return self.render_to_response(self.get_context_data(form=form))
