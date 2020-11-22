from django.contrib import admin
from .models import Profile, Day_off, Type_day_off, Overwork, Type_overwork, Amount_hour, \
    Departament, Rank, Departament_name, Status, Permission

# Register your models here.
admin.site.register(Profile)
admin.site.register(Day_off)
admin.site.register(Type_day_off)
admin.site.register(Overwork)
admin.site.register(Type_overwork)
admin.site.register(Amount_hour)
admin.site.register(Departament)
admin.site.register(Rank)
admin.site.register(Departament_name)
admin.site.register(Status)
admin.site.register(Permission)
