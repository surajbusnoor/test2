from django import forms
from django.core.validators import ValidationError
from formUser.models import User

#def validateName(value):
 #   if value.isdigit():
  #      raise ValidationError('Digits not allowed!')

#def validateEmail(email):
 #   email = email.lower()
 #   if email.split('@')[1] != 'hpe.com':
 #       raise ValidationError('Enter hpe Email ID')

#def validateCity(city):
#    if city.isdigit():
#        raise ValidationError('Digits not allowed!')


#def validatePin(pin):
#    if pin.isalpha():
#        raise ValidationError('Only Integers are allowed!')


class usrForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'


#class userForm(forms.Form):

#    emp_name=forms.CharField(
#        min_length=8,
#        max_length=20,
       # regex=r'[a-zA-Z0-9_. -]+$',
       # regex=r'^[\w.@+-]+$',
#        label = 'User Name',
#        error_messages= {
#            'required':'User Name cannot be left blank!',
 #           'min_length':'Name should have minimum of 8 characters'
 #       },
 #       validators=[validateName]
#    )
#{% comment %}
#    email=forms.EmailField(
#        validators=[validateEmail]
#    )
#    address = forms.CharField(
#        required=False,
#        widget=forms.Textarea(
#            attrs={
#                "placeholder": "Address",
#                "class": "new-class-name two",
#                "rows": 10,
#                "cols": 60,
#            }
#        )

#    )
 #   city=forms.CharField(
#        validators=[validateCity]
#    )
#{% endcomment %}
   # pin = forms.IntegerField(
    #      validators=[validatePin]
   # )
    #Mobile_Number = forms.RegexField(regex='[0-9]{10,10}')


