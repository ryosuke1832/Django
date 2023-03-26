from django import forms

class WellcmForm(forms.Form):
    name = forms.CharField(label='お名前')
    mail = forms.CharField(label='メール')
    age = forms.IntegerField(label='御年齢')