from django.shortcuts import render

# Create your views here.
def dashboard(request):
  # 대시보드 변수저장
  data = "대시보드"
  # 대시보드 글자를 html 랜더링
  # request에대해서 응답해 주기
  # return render(request, '템플릿', {"key":data})
  return render(request, 'dashboard/dashboard.html', {"key":data})

