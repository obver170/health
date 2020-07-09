from django.shortcuts import render
from .models import Arterial, Blood
from .forms import ArterialForm, BloodForm
from .code.arterial_pressure import ArterialCheck
from .code.blood_check import BloodCheck
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
            # print(arterial.problem)
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

@login_required
def get_blood(request):
    person = Person.objects.get(user=request.user)

    # Получаю текущий возраст в int
    today = date.today()
    age = today.year - person.dob.year

    if request.method == "POST":
        form = BloodForm(request.POST)
        if form.is_valid():

            blood = form.save(commit=False)
            blood.person = request.user
            blood.sex = person.sex

            b = BloodCheck(blood.sex, blood.RBC, blood.MCV, blood.MCH, blood.MCHC, blood.RFV, blood.HGB, blood.HCT,
                           blood.CP, blood.PLT, blood.ESR, blood.MPV, blood.WBC)

            check = b.get_blood_check()

            blood.problem = check['problem']

            if blood.problem:
                if 'check_ESR' in check:
                    blood.problem_ESR = True
                if 'check_HCT' in check:
                    blood.problem_HCT = True
                if 'check_HGB' in check:
                    blood.problem_HGB = True
                if 'check_RBC' in check:
                    blood.problem_RBC = True
                if 'check_CP' in check:
                    blood.problem_CP = True
                if 'check_PLT' in check:
                    blood.problem_PLT = True
                if 'check_MPV' in check:
                    blood.problem_MPV = True
                if 'check_WBC' in check:
                    blood.problem_WBC = True


            blood.fast_check = check

            blood.save()

    bloods = Blood.objects.filter(person=request.user)
    form = BloodForm()

    context = {
        'bloods': bloods,
        'form': form,
        'person': person,
        'age': age,
    }
    return render(request, 'monitor/blood.html', context)
