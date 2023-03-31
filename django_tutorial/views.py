from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from .forms import CreateUserForm
from django.shortcuts import render
from community.models import Article

# http://127.0.0.1:8000/
# 홈 처리 함수
def home(request):
    # print(Article.objects.all().order_by('-cdate')[:3])
    articles = Article.objects.all().order_by('-cdate')[:3]
    return render(request, 'index.html', {"articles": articles})


class UserCreateView(CreateView):
  form_class = CreateUserForm
  template_name = 'registration/register.html'
  success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
  template_name = 'registration/register_done.html'