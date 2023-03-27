from django.shortcuts import render

# Create your views here.
def write(request):
    
    # 방법1
    name = "joy"
    title = "오늘 저녁에 운동하기"
    content = "친구랑 함께 한강변을 걷기로함"

    # return render(request, 'write.html', {
    #     "name": name, 
    #     "title": title, 
    #     "content":content})

    # 방법2
    context =  {
      "name" : name, 
      "title" : title, 
      "content" : content
    }
    return render(request, 'write.html', context)

