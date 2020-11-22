from datetime import date, datetime

today = date.today()
month = today.month
year = today.year

# Метод принимает список, переработки или отгулов. Возвращает результат в зависимости от поля status
def get_list_status_Bool(list, bool):
    res = []
    for i in list:
        try:
            if i.status == bool:
                res.append(i)
        except:
            print("Неправильный тип списка")
    return res

# Метод принимает список, переработки или отгулов. Возвращает результат в зависимости от поля Is_true
def get_list_isTrue_Bool(list, bool):
    res = []
    for i in list:
        try:
            if i.is_True == bool:
                res.append(i)
        except:
            print("Неправильный тип списка")
    return res

# Метод для определения дат выходных дней в указанном месяце
def get_vacation_month(year, month):
    vacation = []
    for i in range(1, 32, 1):
        try:
            dt = datetime(year, month, i)
            if dt.isoweekday() == 6 or dt.isoweekday() == 7:
                vacation.append(i)
        except ValueError:
            return vacation


# Метод для получения списка переработки или отгулов по месяцу и году
def get_list_month(list, month, year):
    res = []
    for i in list:
        if i.date.month == month and i.date.year == year:
            res.append(i)
            print(i)
    return res


# Метод для определения количества выходных в текущем месяце
def get_my_vacation(overwork, day_off):
    # Определяю даты выходных дней в текущем месяце
    vacation = get_vacation_month(year, month)
    # Исключаю из выходных даты, где есть переработка
    for over in overwork:
        if over.date.day in vacation:
            vacation.remove(over.date.day)
    # Добавляю отгулы
    for day in day_off:
        vacation.append(day.date.day)
    return vacation



