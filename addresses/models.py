from django.db import models
from users.models import User

# Create your models here.
class Address(models.Model):
    user            =       models.ForeignKey(User, on_delete=models.CASCADE)
    full_name       =       models.CharField(max_length=255)
    phone           =       models.CharField(max_length=15)
    street_address  =       models.CharField(max_length=255)
    city            =       models.CharField(max_length=100)
    state           =       models.CharField(max_length=100)
    postal_code     =       models.CharField(max_length=20)
    country         =       models.CharField(max_length=100)
    is_default      =       models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.street_address}"