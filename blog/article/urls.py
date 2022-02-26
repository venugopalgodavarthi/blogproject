from django.urls import path
from article import views
app_name = 'article'


urlpatterns = [
    path('addarticle/', views.addarticle, name='addarticle'),
    path('modifyarticle/<pk>/', views.modifyarticle, name='modifyarticle'),
    path('deletearticle/<pk>/', views.deletearticle, name='deletearticle'),
    path('index/', views.indexview, name='index'),
    path('articleview/<pk>/', views.articleview, name='articleview'),



]
