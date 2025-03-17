from django.contrib.auth.hashers import make_password, check_password
from django.db import models

IS_ACTIVE_CHOICES = (
    (0, 'false'),
    (1, 'true'),
)


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, unique=True, verbose_name="acounts")
    password = models.CharField(max_length=500, verbose_name="password")
    email = models.CharField(max_length=254, verbose_name="email")
    name = models.CharField(max_length=20, verbose_name="name")
    phone = models.CharField(max_length=20, verbose_name="tel")
    address = models.CharField(max_length=200, verbose_name="address")
    is_active = models.IntegerField(verbose_name="is", default=True, choices=IS_ACTIVE_CHOICES)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "phone": self.phone,
            "address": self.address,
            "email": self.email,
            "is_active": self.is_active,
        }

    # set password
    def set_password(self, password):
        self.password = make_password(password)
        self.save()

    # check password
    def check_password(self, password):
        return check_password(password, self.password)
