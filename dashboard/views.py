from django.shortcuts import render
from .models import CountryData
from .forms import CountryDataForm
# Create your views here.
def dashboard(request):
  if request.method == "POST":
    form  = CountryDataForm(request.POST)
    # print(form)
    if form.is_valid():

      # 폼에 입력 값을 개별로 변수 대입
      input_country = form.data.get('country', None)
      input_num = form.data.get('population', None)

      # CountryData에 연결된 db에 입력 데이터가 있으면 update, 
      # 없으면 create하는 로직
      CountryData.objects.update_or_create(
          # filter : 중복을 체크할 값
          # country : CountryData 클래스의 속성 => 연결된 테이블의 country 속성
          # country의 값과 입력을 비교함, 값이 있는지 없는지 체크하는 역할
          country = input_country,

          # form에서 입력한 country의 값이 없으면 테이블에 저장하도록함
          #new value :
          defaults = {
              'country': input_country,
              'population': input_num          
          }
      )
      # form 객체의 데이터 테이블에 무조건 저장
      # form.save()

  # db : CountryData 클래스를 통해 DB 데이터 가져오기
  # 쿼리 데이터 변수에 대입
  country_datas = CountryData.objects.all()
  # print(country_datas)
    # form 객체 생성
  form = CountryDataForm()

  # 가장 인구 많은 나라와 그 나라의 인구
  from django.db.models import Max, Sum
  max_pop = CountryData.objects.aggregate(Max('population'))
  # print(pop_max)
  max_pop = CountryData.objects.get(population=max_pop['population__max'])
  # print(int(float(max_pop)))
  print(type(max_pop))

  # 테이블 population 컬럼의 전체의 인구 총합, 참여한 나라수
  sum_pop = CountryData.objects.aggregate(Sum('population'))
  # print(sum_pop['population__sum'])
  sum_pop = sum_pop['population__sum']
  print(int(sum_pop))

  # 집계한 나라의 수
  cnt_country = CountryData.objects.count()
  print(cnt_country)

  context = {
    "country_datas": country_datas, 
    "form": form,
    "max_pop": max_pop,
    "sum_pop": sum_pop,
    "cnt_country": cnt_country

  }
  return render(request, 'dashboard/dashboard.html', context)

