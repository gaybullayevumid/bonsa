from .models import *
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.


class HomePageView(ListView):
    model = Home
    template_name = "pages/home.html"
    context_object_name = "homes"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class MembersPageView(TemplateView):
    template_name = "pages/members.html"


class PortfolioPageView(TemplateView):
    template_name = "pages/portfolio.html"


class PricingPageView(TemplateView):
    template_name = "pages/pricing.html"


class Error404PageView(TemplateView):
    template_name = "pages/error404.html"


class FaqPageView(TemplateView):
    template_name = "pages/faq.html"


class TermsConditionPageView(TemplateView):
    template_name = "pages/terms-condition.html"


class PrivacyPolicyPageView(TemplateView):
    template_name = "pages/privacy-policy.html"


class ServicesPageView(TemplateView):
    template_name = "pages/services.html"


class ServiceDetailsPageView(TemplateView):
    template_name = "pages/service-details.html"


class TestimonialPageView(TemplateView):
    template_name = "pages/testimonial.html"


class ContactPageView(ListView):
    model = ContactInfo
    template_name = "pages/contact.html"
    context_object_name = "contacts"