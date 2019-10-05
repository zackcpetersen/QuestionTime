from django_registration.forms import RegistrationForm
from users.models import CustomUser


class CustomUserForm(RegistrationForm):

    class meta(RegistrationForm.Meta):
        model = CustomUser
