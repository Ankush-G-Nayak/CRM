from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record
from django.core.validators import RegexValidator
class Userform(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields=['username','email','password1','password2']

class Addcutstomer(forms.ModelForm):
    Created=forms.DateTimeField(required=True,widget=forms.widgets.TextInput(attrs={'type':'date','placeholder':'','class':'form-control'}),label='')
    username=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Username','class':'form-control'}),label='')
    email=forms.EmailField(required=True,widget=forms.widgets.EmailInput(attrs={'placeholder':'Email','class':'form-control'}),label='')
    PhNo=forms.CharField(required=True,
                         widget=forms.widgets.TextInput(attrs={'placeholder':'PhNo','class':'form-control'}),
                         label='',
                         max_length=10,
                         validators=[RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit phone number')]
                         )

    class Meta():
        model=Record
        exclude=('user',)

class Updatecutstomer(forms.ModelForm):
    username = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
        label=''
    )
    email = forms.EmailField(
        required=True,
        widget=forms.widgets.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        label=''
    )
    PhNo = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={'placeholder': 'PhNo', 'class': 'form-control'}),
        label='',
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit phone number')]
    )

    class Meta:
        model = Record
        exclude = ('user', 'created')