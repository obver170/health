from django.urls import path

from .views import index, bp

app_name = 'monitor'

urlpatterns = [
    path('', index, name='index'),
    path('bp/', bp, name='bp'),
]