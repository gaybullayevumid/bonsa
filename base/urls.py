from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('members/', MembersPageView.as_view(), name='members'),
    path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
    path('pricing/', PricingPageView.as_view(), name='pricing'),
    path('404/', Error404PageView.as_view(), name='404'),
    path('faq/', FaqPageView.as_view(), name='faq'),
    path('sign_in/', SignInPageView.as_view(), name='sign-in'),
    path('sign_up/', SignUpPageView.as_view(), name='sign-up'),
    path('recover_password/', RecoverPasswordPageView.as_view(), name='recover_password'),
    path('terms_condition/', TermsConditionPageView.as_view(), name='terms_condition'),
    path('privacy_policy/', PrivacyPolicyPageView.as_view(), name='privacy_policy'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('service_details/', ServiceDetailsPageView.as_view(), name='service_details'),
    path('testimonial/', TestimonialPageView.as_view(), name='testimonial'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('blog-details/<slug:slug>/', BlogDetailPageView.as_view(), name='blog_details'),
    path('contact/', ContactPageView.as_view(), name='contact'),






]