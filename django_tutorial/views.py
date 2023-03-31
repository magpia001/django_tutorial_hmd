from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from .forms import CreateUserForm


class UserCreateView(CreateView):
  form_class = CreateUserForm
  template_name = 'registration/register.html'
  success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
  template_name = 'registration/register_done.html'