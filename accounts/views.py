from django.contrib.auth import user_logged_in
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class SignInPageView(TemplateView):
    template_name = 'account/sign-in.html'

class SignUpPageView(TemplateView):
    template_name = 'account/sign-up.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserCreationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})

class RecoverPasswordPageView(TemplateView):
    template_name = 'account/recover-password.html'