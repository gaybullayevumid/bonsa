from django.urls import path
from .views import *

urlpatterns = [
    path('sign_in/', SignInPageView.as_view(), name='sign-in'),
    path('sign_up/', SignUpPageView.as_view(), name='sign-up'),
    path('recover_password/', RecoverPasswordPageView.as_view(), name='recover_password')
]