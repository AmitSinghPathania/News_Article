from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_articles, name='search_articles'),
    path('results/', views.results, name='results'),
    path('show/', views.show, name='show'),
    ]
