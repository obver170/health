from django import forms
from .models import Overwork, Type_overwork, Amount_hour, Day_off


class OverworkForm(forms.ModelForm):
    class Meta:
        model = Overwork
        fields = ('date', 'type_overwork', 'amount_hour',)

class Type_overworkForm(forms.ModelForm):
    class Meta:
        model = Type_overwork
        fields = ('name_type', 'description_type',)

class Day_offForm(forms.ModelForm):
    class Meta:
        model = Day_off
        fields = ('date', 'type_day_off', 'amount_hour',)
