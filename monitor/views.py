from django.shortcuts import render
from .models import Arterial
from .forms import ArterialForm
from .code.arterial_pressure import ArterialCheck
from account.models import Person
from django.contrib.auth.decorators import login_required
from datetime import date



@login_required
def index(request):
    person = Person.objects.get(user=request.user)

    # Получаю текущий возраст в int
    today = date.today()
    age = today.year - person.dob.year

    context = {
        'person': person,
        'age':age,
    }
    return render(request, 'monitor/index.html', context)

@login_required
def get_articles(request):
    person = Person.objects.get(user=request.user)

    # Получаю текущий возраст в int
    today = date.today()
    age = today.year - person.dob.year

    context = {
        'person': person,
        'age': age,
    }
    return render(request, 'monitor/articles.html', context)

@login_required
def get_blood(request):
    person = Person.objects.get(user=request.user)

    # Получаю текущий возраст в int
    today = date.today()
    age = today.year - person.dob.year

    context = {
        'person': person,
        'age': age,
    }
    return render(request, 'monitor/blood.html', context)


@login_required
def get_bp(request):
    person = Person.objects.get(user=request.user)

    # Получаю текущий возраст в int
    today = date.today()
    dob = person.dob
    age = today.year - dob.year

    if request.method == "POST":
        form = ArterialForm(request.POST)
        if form.is_valid():

            arterial = form.save(commit=False)
            arterial.person = request.user
            arterial.name = person.name
            arterial.sex = person.sex
            arterial.age = age
            a = ArterialCheck()

            check = a.final_check(arterial.sex, arterial.age, arterial.top_pressure,
                                                arterial.bottom_pressure)

            arterial.problem = check.get('problem')
            print(arterial.problem)
            arterial.fast_check = check.get('diagnosis')
            arterial.save()

    pressure = Arterial.objects.filter(person=request.user)
    form = ArterialForm()
    context = {'pressure': pressure,
               'form': form,
               'person': person,
               'age': age
               }

    return render(request, 'monitor/bp.html', context)
