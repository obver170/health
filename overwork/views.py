from datetime import date
from django.http import HttpResponse

from django.shortcuts import render
from .models import Profile, Day_off, Type_day_off, Overwork, Type_overwork, Amount_hour, \
    Departament, Rank, Departament_name, Status, Permission
from account.models import Person
from django.contrib.auth.decorators import login_required
from .forms import OverworkForm, Type_overworkForm, Day_offForm
from .code.time_tools import get_list_status_Bool, get_list_isTrue_Bool, get_list_month, get_my_vacation


# Create your views here.


@login_required
def dashboard(request):
    # Страница для отбражения общей информации о переработке сотрудника (количество заявок,
    # количество принятых, отклоненных, непроверенных, общее количество переработки.
    # Количество выходных в текущем месяце, среднее время отдыха за месяц и год
    # Содержит статистику переработки/отгулам по месяцам, и текущему году.
    # Ссылки на добавление переработки и отгулов, ссылки на все отгулы и все переработки.
    # Если это админ то ссылки на проверку отгулов и переработки.
    # Ссылку на личный состав, находящийся в подчинении, со статистикой

    person = Person.objects.get(user=request.user)
    profile = Profile.objects.get(person=person)

    today = date.today()
    month = today.month
    year = today.year

    departament = profile.departament.name_departament
    rank = profile.departament.rank

    status = profile.status
    permission = profile.permission

    overwork = Overwork.objects.filter(profile=profile)
    day_off = Day_off.objects.filter(profile=profile)

    # Поиск проверенной переработки
    overwork_verified = get_list_status_Bool(overwork, True)
    # Поиск не проверенной переработки
    overwork_not_verifed = get_list_status_Bool(overwork, False)
    # Поиск отклоненной переработки
    overwork_not_True = get_list_isTrue_Bool(overwork_verified, False)
    # Поиск принятой переработки
    overwork_isTrue = get_list_isTrue_Bool(overwork_verified, True)
    # Переработка в текущем месяце
    overwork_current = get_list_month(overwork_isTrue, month, year)




    # Поиск проверенных отгулов
    day_off_verifed = get_list_status_Bool(day_off, True)
    # Поиск не проверенных отгулов
    day_off_not_verifed = get_list_status_Bool(day_off, False)
    # Поиск отклоненных отгулов
    day_off_not_True = get_list_isTrue_Bool(day_off_verifed, False)
    # Поиск принятых отгулов
    day_off_isTrue = get_list_isTrue_Bool(day_off_verifed, True)
    # Отгулы в текущем месяце
    day_off_current = get_list_month(day_off_isTrue, month, year)

    my_vacations = get_my_vacation(overwork_isTrue, day_off_current)



    context = {'today': today,
               'profile': profile,
               'departament': departament,
               'overwork': overwork,
               'day_off': day_off,
               'rank': rank,
               'overwork_verified': overwork_verified,
               'overwork_not_verifed': overwork_not_verifed,
               'day_off_verifed': day_off_verifed,
               'day_off_not_verifed': day_off_not_verifed,
               'overwork_not_True': overwork_not_True,
               'overwork_isTrue': overwork_isTrue,
               'day_off_not_True': day_off_not_True,
               'day_off_isTrue': day_off_isTrue,
               'overwork_current': overwork_current,
               'day_off_current': day_off_current,
               'my_vacations': my_vacations,
               }

    return render(request, 'overwork/dashboard.html', context)


@login_required
def add_overwork(request):
    person = Person.objects.get(user=request.user)
    profile = Profile.objects.get(person=person)

    if request.method == "POST":
        form = OverworkForm(request.POST)
        if form.is_valid():
            overwork = form.save(commit=False)
            overwork.profile = profile
            overwork.save()
    form = OverworkForm()
    context = {'form': form,
               'profile': profile,
               }

    return render(request, 'overwork/add_overwork.html', context)


@login_required
def add_type_overwork(request):
    person = Person.objects.get(user=request.user)
    profile = Profile.objects.get(person=person)
    type = Type_overwork.objects.all()

    if request.method == "POST":
        form = Type_overworkForm(request.POST)
        if form.is_valid():
            type_overwork = form.save(commit=False)
            type_overwork.save()
    form = Type_overworkForm()
    context = {'form': form,
                'profile': profile,
                'type': type,
               }
    return render(request, 'overwork/add_type_overwork.html', context)

@login_required
def add_day_off(request):
    person = Person.objects.get(user=request.user)
    profile = Profile.objects.get(person=person)
    if request.method == "POST":
        form = Day_offForm(request.POST)
        if form.is_valid():
            day_off = form.save(commit=False)
            day_off.profile = profile
            day_off.save()
    form = Day_offForm()
    context = {'form': form,
               'profile': profile,
               }
    return render(request, 'overwork/add_day_off.html', context)


@login_required
def view_my_work_time(request):
    person = Person.objects.get(user=request.user)
    return HttpResponse("Страница показывает все заявки сотрудника, и их статус проверки " + person.name)


@login_required
def admin(request):
    person = Person.objects.get(user=request.user)
    return HttpResponse("Страница для администраторов" + person.name)
