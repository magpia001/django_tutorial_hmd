from django.contrib import admin
from django.urls import path, include
# from community.views import write, list
from community import views 

# from .views import UserCreateView, UserCreateDoneTV
from . import views as av

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 홈 path '/' : 오류남
    # path('', av.home, name="home"),
    # CBV 방식 path
    path('', av.home, name="home"),

    # community 앱의 path를 포함시킴
    path('community/', include('community.urls')),
    path('dashboard/', include('dashboard.urls')),

    # django.contrib.auth.urls 장고 내장 인증 urls 활용
    path('accounts/', include('django.contrib.auth.urls')),

    # 회원가입 처리 path
    # UserCreateView.as_view() : 클래스형 view 호출방법
    path('accounts/register/', av.UserCreateView.as_view(), name="register"),
    # 계정생성이 완료됐다는 메시지를 보여는 path
    path('accounts/register/done/', av.UserCreateDoneTV.as_view(), name='register_done'),
   ]
