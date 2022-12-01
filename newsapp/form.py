from django import forms
from newsapp.models import Topic


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Ім'я користувача")
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторіть пароль', widget=forms.PasswordInput)


class SettingsForm(forms.Form):
    topics = forms.ModelMultipleChoiceField(queryset=Topic.objects.all(), label='Тема')
