from django import forms

class CitySelect(forms.Form):
    city = forms.CharField(label='city', max_length=100)
    