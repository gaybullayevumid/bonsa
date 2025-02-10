from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('404/', error404, name='404'),
    path('about/', about, name='about'),
    path('blog_details/', blog_details, name='blog-details'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('members/', members, name='members'),
    path('portfolio/', portfolio, name='portfolio'),
    path('pricing/', pricing, name='pricing'),
    path('privacy_policy/', privacy_policy, name='privacy-policy'),
    path('recover_password/', recover_password, name='recover-password'),
    path('service_details/', service_details, name='service-details'),
    path('services/', services, name='services'),
    path('sign_in/', sign_in, name='sign-in'),
    path('sign_up/', sign_up, name='sign-up'),
    path('terms_condition/', terms_condition, name='terms-condition'),
    path('testimonial/', testimonial, name='testimonial')
]