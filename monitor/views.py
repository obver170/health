from django.shortcuts import render
from .models import Arterial
from .forms import ArterialForm
from .code import check, ArterialCheck
from account.models import Person
from django.contrib.auth.decorators import login_required

# def index(request):
#     pressure = Arterial.objects.all()
#     form = ArterialForm()
#     context = {'pressure': pressure,
#                'form': form,
#                }
#     return render(request, 'monitor/index.html', context)


@login_required
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
    person = Person.objects.get(pk=1)
    context = {'pressure': pressure,
                   'form': form,
               'person': person,
                }

    return render(request, 'monitor/index.html', context)