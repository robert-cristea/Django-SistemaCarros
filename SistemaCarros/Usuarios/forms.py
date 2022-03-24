from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm


#registro
class RegisterForm(UserCreationForm):
    username=forms.CharField(label="Usuario",widget=forms.TextInput(attrs={'class': 'form-control'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    taller=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center'}),
    )
    password2 = forms.CharField(
        label="Confirma Contraseña",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center'}),
    )


    class Meta:
        model=User
        fields=['username','email','telefono','taller']
        widgets = {
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }


#change password

class PasswordChangingForm(PasswordChangeForm):
    old_password=forms.CharField(label="Contraseña anterior",widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 = forms.CharField(max_length=100,label="Nueva Contraseña",widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2 = forms.CharField(max_length=100,label="Confirma tu Nueva Contraseña",widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))

    class Meta:
        model=User
        fields=('old_password','new_password1','new_password2')










