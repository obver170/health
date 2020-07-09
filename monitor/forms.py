from django import forms
from .models import Arterial, Blood


class ArterialForm(forms.ModelForm):
    # top_pressure = forms.IntegerField(label='Верхнее давление', initial=120)
    # bottom_pressure = forms.IntegerField(label='Нижнее давление', initial=80)

    class Meta:
        model = Arterial
        fields = ('top_pressure', 'bottom_pressure',)


class BloodForm(forms.ModelForm):
    class Meta:
        model = Blood
        fields = ('RBC', 'MCV', 'MCH', 'MCHC', 'RFV', 'HGB', 'HCT', 'CP', 'PLT', 'ESR', 'MPV', 'WBC')
