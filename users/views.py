from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from users.forms import CustomUserChangeForm
from users.models import CustomUser


class AccountDetailView(LoginRequiredMixin, TemplateView):
    template_name = "users/account.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        return context


class EmailView(TemplateView):
    template_name = "users/e-mail.html"


class PasswordView(TemplateView):
    template_name = "users/password.html"


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = "users/profile.html"
    success_url = reverse_lazy('users:account')

    def get_object(self, queryset=None):
        return self.request.user


class ActionListView(TemplateView):
    template_name = "users/viewhistory.html"
