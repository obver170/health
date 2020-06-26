# Класс для анализа артериального давления, информацию брал с сайта
# https://yandex.ru/turbo/s/giperton.com/norma-arterialnogo-davleniya-u-cheloveka.html
class ArterialCheck:
    # Проверка артериального давления
    def final_check(self, sex, age, t_press, b_press):
        age = int(age)
        if sex == 'Мужчина':
            result = self.m_check(age, t_press, b_press)
        else:
            result = self.w_check(age, t_press, b_press)
        return result

    # служебный метод, проверка АД у мужчин, в зависимости от возраста
    def m_check(self, age, t_press, b_press):
        result = 'Диагностировать состояние АД не удалось'
        if age <= 20:
            t_normal = 123
            b_normal = 76
            result = self.arterial_check(t_press, t_normal, b_press, b_normal)
        elif 20 < age <= 30:
            t_normal = 126
            b_normal = 79
            result = self.arterial_check(t_press, t_normal, b_press, b_normal)
        elif 30 < age <= 40:
            t_normal = 129
            b_normal = 81
            result = self.arterial_check(t_press, t_normal, b_press, b_normal)
        elif 40 < age <= 50:
            t_normal = 135
            b_normal = 83
            result = self.arterial_check(t_press, t_normal, b_press, b_normal)
        elif 50 < age <= 60:
            t_normal = 142
            b_normal = 85
            result = self.arterial_check(t_press, t_normal, b_press, b_normal)
        elif age > 60:
            t_normal = 142
            b_normal = 80
            result = self.arterial_check(t_press, t_normal, b_press, b_normal)

        return result

    # служебный метод, проверка АД у женщин, в зависимости от возраста
    def w_check(self, age, t_press, b_press):
        result = 'Давление в норме'
        if age <= 20:
            t_normal = 116
            b_normal = 72
            result = self.arterial_check(t_press, t_normal, b_press, b_normal)
        elif 20 < age <= 30:
            t_normal = 120
            b_normal = 75
            result = self.arterial_check(t_press, t_normal, b_press, b_normal)
        elif 30 < age <= 40:
            t_normal = 127
            b_normal = 80
            result = self.arterial_check(t_press, t_normal, b_press, b_normal)
        elif 40 < age <= 50:
            t_normal = 137
            b_normal = 84
            result = self.arterial_check(t_press, t_normal, b_press, b_normal)
        elif 50 < age <= 60:
            t_normal = 144
            b_normal = 85
            result = self.arterial_check(t_press, t_normal, b_press, b_normal)
        elif age > 60:
            t_normal = 159
            b_normal = 85
            result = self.arterial_check(t_press, t_normal, b_press, b_normal)
        return result

    # Служебный метод, проверяет вхождение текущего давления в безопасный диапазон, диагностирует Гипертонию и Гипотонию
    def arterial_check(self, t_press, t_normal, b_press, b_normal):
        result = 'Артериальное давление в норме'
        t_safe_range = self.safe_range('top', t_normal)
        b_safe_range = self.safe_range('bottom', b_normal)
        if t_press in t_safe_range and b_press in b_safe_range:
            return result
        else:
            result = 'Обнаруженны проблемы с артериальным давлением'
            if t_press > t_safe_range[-1] or b_press > b_safe_range[-1]:
                result = 'Обнаруженны проблемы с артериальным давлением. Предполагается гипертония'
            if t_press < t_safe_range[0] or b_press < b_safe_range[0]:
                result = 'Обнаруженны проблемы с артериальным давлением. Предполагается гипотония'
        return result

    # служебный метод, возвращает диапазон безопасного значения АД в зависимости от того верхнее оно или нижнее
    def safe_range(self, pressure, start):
        if pressure == 'top':
            return self.get_range(start - 3, start + 10)
        else:
            return self.get_range(start - 1, start + 5)

    # служебный метод, возвращает список чисел, начиная от указанного до конечного числа
    def get_range(self, start, end):
        diapason = [i for i in range(start, end)]
        return diapason
