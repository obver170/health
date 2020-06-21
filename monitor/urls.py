from django.urls import path

from .views import index

app_name = 'monitor'

urlpatterns = [
    path('', index, name='index'),
    path('bp/', index, name='bp'),
]