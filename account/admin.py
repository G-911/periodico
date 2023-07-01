from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here idiot.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm 
    model = CustomUser
    list_display = [
        "email",
        "username",
        "password",
        "age",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields" : ("age", )}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields" : ("age", )}),)


admin.site.register(CustomUser, CustomUserAdmin)