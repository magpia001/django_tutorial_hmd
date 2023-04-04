from django.contrib import admin
from .models import CountryData

# Register your models here.

# admin site dashbord list ui 바꾸기
# UI 변경 클래스 정의
## admin.ModelAdmin 상속 받기
# admin.site.register(모델클래스, UI재정의클래스)

class DashboardAdmin(admin.ModelAdmin):
    list_display = ('country', 'population')
    
admin.site.register(CountryData, DashboardAdmin)
