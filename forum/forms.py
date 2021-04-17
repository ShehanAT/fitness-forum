from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import ForumUser
from django.core.validators import validate_email
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.exceptions import ValidationError
from ckeditor.widgets import CKEditorWidget 

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
    message = forms.CharField(widget=CKEditorWidget())

class ForumUserForm(forms.Form):
    '''Form for the image model'''
    profic_pic = forms.ImageField(label='Profilc Picture') 

class MultiEmailField(forms.Field):
    def to_python(self, value):
        if not value:
            return []
        return value.split(',')
    
    def validate(self, value):
        super().validate(value)
        for email in value:
            validate_email(email)

class UpdateProfileForm(forms.ModelForm):
    password = None
    username = forms.CharField(max_length=250)
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = ForumUser 
        fields = [
            'username',
            'email',
            'first_name',
            'last_name'
        ]

class ProfilePicForm(forms.Form):
    profile_pic = forms.ImageField(label='Profile Picture Upload')
    
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'})

    class Meta:
        model = User 
        fields = (
            'old_password',
            'new_password',
            'new_password_confirm'
        )

class PostSignatureForm(forms.Form):
    content = forms.CharField(widget=CKEditorWidget())