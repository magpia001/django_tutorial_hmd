from django.forms import ModelForm
from .models import CountryData

class CountryDataForm(ModelForm):
    class Meta:
        model = CountryData
        # CountryData 클래스의 모든 속성을 form field로 사용
        fields = '__all__'