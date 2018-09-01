from django import forms

class form1(forms.Form):
    Mobile= forms.IntegerField()
    Email = forms.EmailField()
    Date=forms.DateField()