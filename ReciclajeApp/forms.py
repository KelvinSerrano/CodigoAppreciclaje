from django import forms
from ReciclajeApp.models import ClaseCuentaB
from ReciclajeApp.models import ClaseContacto
from ReciclajeApp.models import ClaseLogin

class FormCuentaB(forms.ModelForm):
    class Meta:
        model = ClaseCuentaB
        fields = '__all__'

class FormContacto(forms.ModelForm):
    class Meta:
        model = ClaseContacto
        fields = '__all__'

class FormLogin(forms.ModelForm):
    class Meta:
        model = ClaseLogin
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")


