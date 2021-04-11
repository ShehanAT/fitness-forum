from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image, ForumUser
 
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')


class AddCategoryForm(forms.Form):
    category_name = forms.CharField(label='New Form Category', max_length=100)
    category_description = forms.CharField(label='New Form Description', max_length=500)
    
class AddThreadForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', max_length=500)
    
class AddPostForm(forms.Form):
    message = forms.CharField(label='Message', max_length=500)

class ForumUserForm(forms.Form):
    '''Form for the image model'''
    profic_pic = forms.ImageField(label='Profilc Picture') 

class ProfilePicForm(forms.Form):
    # class Meta:
    #     model = ForumUser 
    #     fields = ['profile_pic']
    profile_pic = forms.ImageField(label='Profile Picture Upload')