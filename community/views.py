from django.shortcuts import render, redirect
from community.forms import Form
from .models import Article

# http://127.0.0.1:8000/
# 홈 처리 함수
def home(request):
    # print(Article.objects.all().order_by('-cdate')[:3])
    articles = Article.objects.all().order_by('-cdate')[:3]
    return render(request, 'index.html', {"articles": articles})

# http://127.0.0.1:8000/write/
def write(request):
    # 입력한 form 데이터를 받아서 DB에 저장
    if request.method == 'POST':
        form = Form(request.POST)
        print("POST 데이터 ")
        print(form)
        # form 데이터의 유효성 검사
        if form.is_valid():
            # form 데이터 저장
            form.save()
            return redirect('/write')
    else:
        # 빈 form으로 응답하기
        form = Form()
        # print(form)
        # 사용자 http 요청(request)에 대해서 response해주는 기능
        #   return render(request, 'html 템플릿파일', {"키": 값})
        return render(request, 'write.html', {"form": form})
    
# list : db의 목록을 보여줌
def list(request):
    # community앱, Article 테이블의 데이터 목록 읽어오기
    article_list = Article.objects.all()
    return render(request, 'list.html', {"article_list":article_list})

# list의 detail : 한 항목의 세부내용을 읽어서 응답하기
# path('view_detail/<int:num>/', views.viewDetail, name="view_detail"),
# num 값을 키워드로 넣어주기, urls.py의 num변수는 함수의 keyword 변수와 동일해야함
def viewDetail(request, num=1):
    #  한 항목의 세부내용을 읽어오기
    article_deatil = Article.objects.get(id=num)
    return render(request, 'view_detail.html', {"article":article_deatil})
