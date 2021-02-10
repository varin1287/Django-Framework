from authapp.forms import UserRegisterForm
from django import forms
from authapp.models import User

class AdminUserRegisterForm(UserRegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'avatar', 'age')

    def __init__(self, *args, **kwargs):
        super(AdminUserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'



