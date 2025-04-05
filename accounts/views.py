from django.views.generic import TemplateView

# Create your views here.

class SignInPageView(TemplateView):
    template_name = 'account/sign-in.html'

class SignUpPageView(TemplateView):
    template_name = 'account/sign-up.html'

class RecoverPasswordPageView(TemplateView):
    template_name = 'account/recover-password.html'