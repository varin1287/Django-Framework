from authapp.forms import UserRegisterForm, UserProfileForm
from django import forms
#from authapp.models import User

class AdminUserRegisterForm(UserRegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput())

    # В UserRegisterForm есть все поля
    #class Meta:
    #    model = User
    #    fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'avatar', 'age')

    def __init__(self, *args, **kwargs):
        super(AdminUserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'


class AdminUserProfileForm(UserProfileForm):

    def __init__(self, *args, **kwargs):
        super(AdminUserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False

