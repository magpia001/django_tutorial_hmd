from django.urls import path
# from community.views import write, list
from community import views
 
# app_name="community"    
urlpatterns = [
    # write/ 요청이 들어오면, views.write()함수 실행
    # path('write/', views.write, name="wirte"),
    path('write/', views.WriteFormView.as_view(), name="wirte"),
    # community/list/
    # path('lists/', views.list, name="list"),
    path('lists/', views.ArticleListView.as_view(), name="list"),
    # view_detail/4
    # path('view_detail/<int:num>/', views.viewDetail, name="view_detail"),
    path('view_detail/<int:pk>/', views.ArticleViewDetail.as_view(), name="view_detail"),
]