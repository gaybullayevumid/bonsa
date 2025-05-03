from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic import FormView, View
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm, CustomPasswordResetForm
from django.contrib.auth.views import PasswordResetView as DjangoPasswordResetView, PasswordResetDoneView as DjangoPasswordResetDoneView

# Create your views here.

User = get_user_model()

class UserRegisterView(FormView):
    template_name = 'account/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return super().form_valid(form)

class UserLoginView(FormView):
    template_name = 'account/sign-in.html'
    form_class = LoginForm

    def form_valid(self, form):
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user:
            login(self.request, user)
            return redirect('home')
        form.add_error(None, "Username yoki parol xato")
        return self.form_invalid(form)

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class PasswordResetView(DjangoPasswordResetView):
    template_name = 'account/recover-password.html'
    form_class = CustomPasswordResetForm
    email_template_name = 'account/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class PasswordResetDoneView(DjangoPasswordResetDoneView):
    template_name = 'account/password_reset_done.html'