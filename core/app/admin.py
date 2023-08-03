from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
# from django import forms
from .models import User, Profile


# class CustomUserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='password', widget=forms.PasswordInput)



class CustomeUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    model = User
    # add_form = CustomUserCreationForm
    list_display = ['email', 'is_superuser', 'is_active','is_verified']
    list_filter = ['email', 'is_superuser', 'is_active','is_verified']
    search_fields = ['email',]
    ordering = ['email',]
    fieldsets = (
        ('Authentication', {
            "fields": (
                'email', 'password'
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_staff', 'is_active', 'is_superuser', 'is_verified'
            ),
        }),
        ('group permissions', {
            "fields": (
                'groups', 'user_permissions'
            ),
        }),
        ('important_date', {
            "fields": (
                'last_login',
            ),
        }),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ('wide',),
            "fields": (
                'email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser','is_verified'
            ),
        }),
    )

admin.site.register(Profile)
admin.site.register(User, CustomeUserAdmin)



