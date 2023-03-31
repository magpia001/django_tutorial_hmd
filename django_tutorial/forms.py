from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
  email = forms.EmailField(required=True)
  class Meta:
    model = User   # 장고 제공 model
    # fields = ("username", "email", "password1", "password2")
    fields = ["username", "email", "password1", "password2"]