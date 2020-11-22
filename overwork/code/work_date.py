from datetime import  datetime

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
