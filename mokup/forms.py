from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import food

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='')
    password1 = forms.CharField(widget=forms.PasswordInput, help_text='')  # Optionally hide password input
    password2 = forms.CharField(widget=forms.PasswordInput, help_text='')
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'formInput'}),
            'email': forms.EmailInput(attrs={'class': 'formInput'}),
            'password1': forms.PasswordInput(attrs={'class': 'formInput'}),
            'password2': forms.PasswordInput(attrs={'class': 'formInput'})
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('A user with this email address already exists.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username

class UserLoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'formInput'}),
            'password': forms.PasswordInput(attrs={'class': 'formInput'}),
        }

class FoodForm(forms.ModelForm):
    class Meta:
        model = food
        fields = ['name', 'desc', 'category', 'kcal', 'proteins', 'fats', 'carbs']
