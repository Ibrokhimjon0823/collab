from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'email', 'name', 'is_active',  'is_staff'
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        fields = (
            'email', 'name', 'is_active', 'is_staff'
        )
