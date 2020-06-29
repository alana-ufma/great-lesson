from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django import forms
from django.contrib.auth import get_user_model
from core.mail import send_mail_template
from core.utils import generate_hash_key
from .models import PasswordReset

User = get_user_model()



class PasswordResetForm(forms.ModelForm):
    email = forms.EmailField(widget = forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'E-mail'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = User.objects.filter(email=email)
        if queryset.exists():
            return email
        raise forms.ValidationError('Não existe usuário com este email')

    def save(self):
        context = {}
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        # Enviar Email
        template_email = 'accounts/password_reset_mail.html'
        subject = 'Recuperar Senha na GReAT'
        context['reset']  = reset
        send_mail_template(subject, template_email, context, [user.email])


    class Meta:
        model = PasswordReset
        fields = ['email']


class RegisterForm(forms.ModelForm):
    name = forms.CharField(label = 'Nome',widget = forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Nome'}))
    username = forms.CharField(label = 'Usuário', widget = forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Usuário'}))
    password1 = forms.CharField(label = 'Senha', widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg','placeholder':'Senha'}))
    password2 = forms.CharField(label = 'Confirmação de Senha', widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg','placeholder':'Confirmar Senha'}))
    email = forms.EmailField(widget = forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'E-mail'}))


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A confirmação não está correta')
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['name','username', 'email']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Usuário'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control form-control-lg','placeholder':'Senha'}))


class ChangePasswordForm(PasswordChangeForm):

    old_password = forms.CharField(label='Senha antiga', widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Senha antiga'}))
    new_password1 = forms.CharField(label='Senha nova', widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Senha nova'}))
    new_password2 = forms.CharField(label='Confirmar senha', widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirmar senha'}))


class PasswordResetFormConfirm(SetPasswordForm):
    new_password1 = forms.CharField(label = 'Senha', widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg','placeholder':'Senha'}))
    new_password2 = forms.CharField(label = 'Confirmação de Senha', widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg','placeholder':'Confirmar Senha'}))
    class Meta:
        model = User

class EditAccountForm(forms.ModelForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Usuário'}))
    name = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Nome'}))
    email = forms.EmailField(widget = forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'E-mail'}))
    # website = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Website'}))

    class Meta:
        model = User
        fields = ['name','username', 'email']
