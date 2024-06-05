from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=128, unique=True)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(null=True)


    def __str__(self) -> str:
        return f"{self.username}"



class City(models.Model):
    title = models.CharField(max_length=128, unique=True)

    def __str__(self) -> str:
        return f"{self.title}"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name="profiles")
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=11, null=True)
