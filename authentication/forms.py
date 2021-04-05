from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    #birthday = forms.DateField(help_text='Required, format: YYYY-MM-DD')
    age = forms.FloatField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'age', 'username', 'password1', 'password2')
