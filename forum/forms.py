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
    category_tags = forms.CharField(label="Tags for new category", max_length=500)

class AddThreadForm(forms.Form):
    subject = forms.CharField(label="Thread Title", max_length=100)
    message = forms.CharField(widget=CKEditorWidget(), label="Original Post message")
    tags = forms.CharField(label="Tags for new post", max_length=500)

    def __init__(self, *args, **kwargs):
        super(AddThreadForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class AddPostForm(forms.Form):
    message = forms.CharField(widget=CKEditorWidget())

class ContactUsForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=200)
    subject = forms.CharField(max_length=500)
    message = forms.CharField(widget=CKEditorWidget())


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
    profile_pic = forms.ImageField(label='Profile Picture Upload')
    # , required=False
    location = forms.CharField() 
    about = forms.Textarea()
    class Meta:
        model = ForumUser 
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'profile_pic',
            'location',
            'about'
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