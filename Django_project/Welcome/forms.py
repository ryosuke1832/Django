from django import forms

class WelcmForm(forms.Form):
    name = forms.CharField(label='お名前')
    mail = forms.CharField(label='メールアドレス')
    age = forms.IntegerField(label='ご年齢')
