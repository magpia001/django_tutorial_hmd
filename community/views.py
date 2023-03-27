from django.shortcuts import render
from community.forms import Form

# Create your views here.

# http://127.0.0.1:8000/write/
def write(request):
    # 입력한 form 데이터를 받아서 DB에 저장
    if request.method == 'POST':
        form = Form(request.POST)
        # form 데이터의 유효성 검사
        if form.is_valid():
            # form 데이터 저장
            form.save()
    form = Form()
    # else:
      # 빈 form으로 응답하기
      # form = Form()
    
    return render(request, 'write.html', {"form": form})
