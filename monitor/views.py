from django.shortcuts import render
from .models import Arterial
from .forms import ArterialForm
from .code import check, ArterialCheck

# def index(request):
#     pressure = Arterial.objects.all()
#     form = ArterialForm()
#     context = {'pressure': pressure,
#                'form': form,
#                }
#     return render(request, 'monitor/index.html', context)

def index(request):
    if request.method == "POST":
        form = ArterialForm(request.POST)
        if form.is_valid():
            arterial = form.save(commit=False)
            arterial.problem = check(arterial.bottom_pressure, arterial.top_pressure)
            a = ArterialCheck()
            arterial.fast_check = a.final_check(arterial.sex, arterial.age, arterial.top_pressure, arterial.bottom_pressure)
            arterial.save()

    pressure = Arterial.objects.all()
    form = ArterialForm()
    context = {'pressure': pressure,
                   'form': form,
                }

    return render(request, 'monitor/index.html', context)