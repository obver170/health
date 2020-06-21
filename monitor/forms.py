from django import forms
from .models import Arterial


class ArterialForm(forms.ModelForm):
    person = forms.IntegerField(label='Профиль', widget=forms.widgets.HiddenInput)
    # Делаю поле скрытым и необязательным
    name = forms.CharField(label='Имя', initial='Василий', required=False, widget=forms.widgets.HiddenInput)
    sex = forms.CharField(label='Пол', max_length=10, required=False, widget=forms.widgets.HiddenInput)
    age = forms.IntegerField(label='Возраст', required=False, widget=forms.widgets.HiddenInput)

    # name = forms.CharField(label='Имя', initial='Василий')
    # sex = forms.ChoiceField(label='Пол', choices=Arterial.SEX_LIST)
    # age = forms.ChoiceField(label='Возраст', choices=Arterial.AGE_LIST)

    top_pressure = forms.IntegerField(label='Верхнее давление', initial=120)
    bottom_pressure = forms.IntegerField(label='Нижнее давление', initial=80)

    class Meta:
        model = Arterial
        # fields = ('name', 'sex', 'age', 'top_pressure', 'bottom_pressure',)
        fields = ('top_pressure', 'bottom_pressure',)
