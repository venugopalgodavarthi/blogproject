from dataclasses import field
from django import forms
from authe.models import registermodel
from django.contrib.auth.hashers import make_password


class registerform(forms.ModelForm):
    class Meta:
        model = registermodel
        fields = ['username', 'first_name', 'last_name',
                  'password', 'email', 'phone', 'age', 'gender']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
