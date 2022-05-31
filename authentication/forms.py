from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from authentication.models import UserPermission

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserPermissionsForm(forms.ModelForm):
    class Meta:
        model = UserPermission
        fields = ['CRM_permission', 'Inventory_permission']