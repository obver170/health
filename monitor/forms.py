from django import forms
from .models import Arterial


class ArterialForm(forms.ModelForm):

    # top_pressure = forms.IntegerField(label='Верхнее давление', initial=120)
    # bottom_pressure = forms.IntegerField(label='Нижнее давление', initial=80)

    class Meta:
        model = Arterial
        fields = ('top_pressure', 'bottom_pressure',)
