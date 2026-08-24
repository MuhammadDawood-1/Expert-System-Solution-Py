from django.db import models

class Reporter(models.Model):
    full_name=models.CharFeild(max_length=70)
    
    
    def __str__(self):
        return self.full_name
    
    
class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter,on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
    
    
from django.contrib import admin

from . import models

admin.site.register(models.Article)


from django.urls imports path   

from . import views
    
 urlpatterns =[
    path("articles/<int:year>/", views.year_archive),#year, 
    path("articles/<int:year>/<int:month>/", views.month_archive),# year plus month
    path("articles/<int:year>/<int:month>/<int:pk>/", views.article_detail), # year , month , primary key
]
    
from django.shortcuts import render

from .models import Article


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {"year": year, "article_list": a_list}
    return render(request, "news/year_archive.html", context)

