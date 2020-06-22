from django.shortcuts import render
from .models import Arterial
from .forms import ArterialForm
from .code import check, ArterialCheck
from account.models import Person
from django.contrib.auth.decorators import login_required
from datetime import date


# def index(request):
#     pressure = Arterial.objects.all()
#     form = ArterialForm()
#     context = {'pressure': pressure,
#                'form': form,
#                }
#     return render(request, 'monitor/index.html', context)
@login_required
def index(request):
    person = Person.objects.get(user=request.user)
    context = {
        'person': person
    }
    return render(request, 'monitor/index.html', context)


@login_required
def bp(request):
    person = Person.objects.get(user=request.user)
    print('!!!!!!!' + str(person.pk))
    name = person.name
    sex = person.sex
    today = date.today()
    dob = person.dob
    user = request.user
    print('!!!!!!!' + str(user) + str(type(user)))
    # Получаю текущий возраст в int
    age = today.year - dob.year


    if request.method == "POST":
        form = ArterialForm(request.POST)
        print("!!!!!!!" + str(form.is_valid))
        if form.is_valid():
            arterial = form.save(commit=False)
            # arterial.person = user.pk
            arterial.name = name
            arterial.sex = sex
            arterial.age = age
            arterial.problem = check(arterial.bottom_pressure, arterial.top_pressure)
            a = ArterialCheck()

            arterial.fast_check = a.final_check(arterial.sex, arterial.age, arterial.top_pressure,
                                                arterial.bottom_pressure)
            arterial.save()

    pressure = Arterial.objects.all()
    form = ArterialForm()
    context = {'pressure': pressure,
               'form': form,
               'person': person,
               'age': age
               }

    return render(request, 'monitor/bp.html', context)
