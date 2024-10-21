from django import forms
from django.contrib.auth.forms import UserCreationForm

from momo_app.models import customer, Login, worker, complaint, add, schedule


class customerform(forms.ModelForm):
    class Meta:
        model= customer
        fields=('__all__')
        exclude = ('user',)

class workerform(forms.ModelForm):
    class Meta:
        model= worker
        fields=('__all__')
        exclude = ('user',)



class LoginRegister(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class complaintform(forms.ModelForm):
    class Meta:
        model = complaint
        fields = ('__all__')
        exclude = ('replay','user')

class addform(forms.ModelForm):
    class Meta:
        model = add
        fields = ('notification',)


class DateInput(forms.DateInput):
    input_type = ('date')


class TimeInput(forms.TimeInput):
    input_type = ('time')

class scheduleform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    startingtime = forms.TimeField(widget=TimeInput)
    endingtime = forms.TimeField(widget=TimeInput)

    class Meta:
        model = schedule
        fields = ('date', 'startingtime', 'endingtime',)







