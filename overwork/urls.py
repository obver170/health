from django.urls import path
from .views import dashboard, add_overwork, add_type_overwork, add_day_off, admin

app_name = 'overwork'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('add_overwork/', add_overwork, name='add_overwork'),
    path('add_type_overwork/', add_type_overwork, name='add_type_overwork'),
    path('add_day_off/', add_day_off, name='add_day_off'),
    path('admin/', admin, name='admin'),
]