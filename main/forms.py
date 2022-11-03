from django.contrib.auth.forms import UserCreationForm, User


class UserLogin(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
