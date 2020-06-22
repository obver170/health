from django.shortcuts import render
from .models import Arterial
from .forms import ArterialForm
from .code import ArterialCheck
from account.models import Person
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib.auth.models import User


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
    name = person.name
    sex = person.sex
    today = date.today()
    dob = person.dob
    # Получаю текущий возраст в int
    age = today.year - dob.year


    if request.method == "POST":
        form = ArterialForm(request.POST)
        print("!!!!!!!" + str(form.is_valid))
        if form.is_valid():

            arterial = form.save(commit=False)
            arterial.name = name
            arterial.sex = sex
            arterial.age = age
            a = ArterialCheck()

            arterial.fast_check = a.final_check(arterial.sex, arterial.age, arterial.top_pressure,
                                                arterial.bottom_pressure)
            arterial.save()

    # user = User.objects.get(pk=request.user.pk)
    #
    # pressure = user.arterial_set.all()

    # pressure = Arterial.objects.all()
    pressure = Arterial.objects.filter(name='Иосиф')
    # print(str(user) + '!!!!!!!!!!!!!!' + str(pressure))
    print('!!!!!!!!!!!!!!' + str(pressure))
    form = ArterialForm()
    context = {'pressure': pressure,
               'form': form,
               'person': person,
               'age': age
               }

    return render(request, 'monitor/bp.html', context)
