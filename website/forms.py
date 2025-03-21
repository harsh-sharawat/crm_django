from django.contrib.auth.forms import  UserCreationForm

from django import forms
from .models import Record
# from django.forms import
from django.contrib.auth.models import User


class Registration_form(UserCreationForm):
    

    first_name = forms.CharField(label = "", max_length=100,widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'First name'}))
    last_name = forms.CharField(label = "", max_length=100,widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Last name'}))
    
    email = forms.EmailField(label = "", widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Email'}))
    username = forms.CharField(label='',max_length=100 , widget=forms.TextInput(attrs={'class':"",'placehoder':"enter Unique User_Name"}))
    # password = forms.PasswordInput(label = "", forms.PasswordInput(attrs={}))

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']

    def __init__(self, *args, **kwargs):
        super(Registration_form, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 100 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


class Add_data(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','email','address','phone','zipcode']
    def __init__(self, *args, **kwargs):
        super(Add_data, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = field
            self.fields[field].label = ""
            
            


        
