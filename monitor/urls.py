from django.urls import path

from .views import index, get_bp, get_articles, get_blood

app_name = 'monitor'

urlpatterns = [
    path('', index, name='index'),
    path('bp/', get_bp, name='bp'),
    path('articles/', get_articles, name='articles'),
    path('blood/', get_blood, name='blood'),
]