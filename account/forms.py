from django import forms
from .models import Users, Posts, Neighborhood, Business, Police_station, Emergency_service,Heath_center
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput

class RegisterForm(forms.ModelForm):
    
    class Meta:
        # password_confirm = forms.CharField(max_length=128,widget=PasswordInput())
        # location = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

        model = Users
        fields = ('name','username','email','location','neighborhood_name','password')
        widgets = {
            'password': forms.PasswordInput(),
            # 'location': forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        }
        labels = {
            'neighborhood_name' : 'Neighborhood Name' 
        }
        '__all__'

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['neighborhood_name'].empty_label = "Select"
        # self.fields['emp_code'].required = False

class LoginForm(forms.ModelForm):
    class Meta:      
        model = Users
        fields = ('username','password')
        widgets = {
            'password': forms.PasswordInput()
        }
        # '__all__'

class PostForm(forms.ModelForm):
    class Meta:      
        model = Posts
        fields = ('title','description','author','neighborhood')
        labels = {
            'description' : 'Message', 
        }
        widgets = {
             'author': forms.HiddenInput(),
             'neighborhood': forms.HiddenInput(),
             'description': forms.Textarea(attrs={'rows':4})
        }
 
     
