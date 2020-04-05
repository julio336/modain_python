from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    phone = CharField(("Phone of User"), blank=True, max_length=10)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
