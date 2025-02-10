from django.shortcuts import render
from .models import Blog

# Create your views here.

def home(req):
    template_name = 'pages/home.html'
    return render(req, template_name,)

def error404(req):
    template_name = 'pages/error404.html'
    return render(req, template_name)

def about(req):
    template_name = 'pages/about.html'
    return render(req, template_name)


def blog(req):
    template_name = 'pages/blog.html'
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(req, template_name, context)


def blog_details(req, pk):
    template_name = 'pages/blog-details.html'
    post = Blog.objects.get(pk=pk)
    # last_posts = Blog.objects.order_by('-created_at')
    context = {
        'post': post,
        # 'last_posts': last_posts
    }
    return render(req, template_name, context)

def contact(req):
    template_name = 'pages/contact.html'
    return render(req, template_name)

def faq(req):
    template_name = 'pages/faq.html'
    return render(req, template_name)

def members(req):
    template_name = 'pages/members.html'
    return render(req, template_name)

def portfolio(req):
    template_name = 'pages/portfolio.html'
    return render(req, template_name)

def pricing(req):
    template_name = 'pages/pricing.html'
    return render(req, template_name)

def privacy_policy(req):
    template_name = 'pages/privacy-policy.html'
    return render(req, template_name)

def recover_password(req):
    template_name = 'pages/recover-password.html'
    return render(req, template_name)

def service_details(req):
    template_name = 'pages/service-details.html'
    return render(req, template_name)

def services(req):
    template_name = 'pages/services.html'
    return render(req, template_name)

def sign_in(req):
    template_name = 'pages/sign-in.html'
    return render(req, template_name)

def sign_up(req):
    template_name = 'pages/sign-up.html'
    return render(req, template_name)

def terms_condition(req):
    template_name = 'pages/terms-condition.html'
    return render(req, template_name)

def testimonial(req):
    template_name = 'pages/testimonial.html'
    return render(req, template_name)