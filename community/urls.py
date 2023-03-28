from django.urls import path
# from community.views import write, list
from community import views

urlpatterns = [
    # write/ 요청이 들어오면, views.write()함수 실행
    path('write/', views.write, name="wirte"),
    # list/
    path('list/', views.list, name="list"),
    # view_detail/4
    path('view_detail/<int:num>/', views.viewDetail, name="view_detail"),
]