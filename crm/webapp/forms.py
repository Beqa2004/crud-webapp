#ჯანგოში ჩაშენებული ფორმები შესავსებად
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from . models import Record


# რეგისტრაციის ფორმა  
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "password1", "password2"]



# ლოგინის ფორმა
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())




#ჩანაწერის დამატების ფორმა
class AddRecordForm(forms.ModelForm): #ModelForm აუტომატურად აგენერირებს ფორმებს მოდელების მიხედვით
    class Meta:
        model = Record
        fields = ['first_name', "last_name", "email", 'phone', 'address', 'city', 'country']


#ინფორმაციის აპდეითი
class UpadteRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', "last_name", "email", 'phone', 'address', 'city', 'country']
