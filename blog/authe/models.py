from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class registermodel(User):
    phone = models.BigIntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[
                              ['MALE', 'Male'], ['FEMALE', 'Female']])

    def __str__(self):
        return self.username
