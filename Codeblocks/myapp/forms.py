from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Room



class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class Roomform(ModelForm):
    class Meta:
        model=Room
        fields= '__all__'
        exclude = ['host','participants']  