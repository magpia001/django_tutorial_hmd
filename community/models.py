from django.db import models

# Create your models here.
class Article(models.Model):
  name = models.CharField(max_length=20)
  title = models.CharField(max_length=50)
  contents = models.TextField()
  url = models.URLField()
  email = models.EmailField()
  cdate = models.DateTimeField(auto_now_add=True)
  
  # 문자열 format : title, name, cdate
  def __str__(self):
    return f"{self.title} : {self.name} : {self.cdate}"