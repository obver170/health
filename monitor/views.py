from django.shortcuts import render
from .models import Arterial, Blood
from .forms import ArterialForm, BloodForm
from .code.arterial_pressure import ArterialCheck
from .code.blood_check_v2 import BloodCheck
from account.models import Person
from django.contrib.auth.decorators import login_required
from datetime import date


@login_required
def index(request):
    person = Person.objects.get(user=request.user)

    # Получаю текущий возраст в int
    today = date.today()
    age = today.year - person.dob.year

    pressure = Arterial.objects.filter(person=request.user).last
    blood = Blood.objects.filter(person=request.user).last


    context = {
        'person': person,
        'age': age,
        'pressure': pressure,
        'blood': blood
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

                marks = check['marks']
                print(check)

                print("!!!!!!" + str(marks))

                if 'over_RBC' in marks or 'under_RBC' in marks:
                    blood.problem_RBC = True
                if 'over_MCV' in marks or 'under_MCV' in marks:
                    blood.problem_MCV = True
                if 'over_MCH' in marks or 'under_MCH' in marks:
                    blood.problem_MCH = True
                if 'over_MCHC' in marks or 'under_MCHC' in marks:
                    blood.problem_MCHC = True
                if 'over_RFV' in marks or 'under_RFV' in marks:
                    blood.problem_RFV = True

                if 'over_ESR' in marks or 'under_ESR' in marks:
                    blood.problem_ESR = True
                if 'over_HCT' in marks or 'under_HCT' in marks:
                    blood.problem_HCT = True
                if 'over_HGB' in marks or 'under_HGB' in marks:
                    blood.problem_HGB = True
                if 'over_CP' in marks or 'under_CP' in marks:
                    blood.problem_CP = True
                if 'over_PLT' in marks or 'under_PLT' in marks:
                    blood.problem_PLT = True
                if 'over_MPV' in marks or 'under_MPV' in marks:
                    blood.problem_MPV = True
                if 'over_WBC' in marks or 'under_WBC' in marks:
                    blood.problem_WBC = True

            # print("!!!!!!" + check['check'])
            blood.fast_check = check['check']

            blood.save()

    bloods = Blood.objects.filter(person=request.user).order_by('-date')
    form = BloodForm()

    context = {
        'bloods': bloods,
        'form': form,
        'person': person,
        'age': age,
    }
    return render(request, 'monitor/blood.html', context)
