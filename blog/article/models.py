from turtle import title
from django.db import models
from authe.models import registermodel
from django.utils import timezone
# Create your models here.


class articlemodel(models.Model):
    author = models.ForeignKey(registermodel, on_delete=models.CASCADE)
    adesc = models.TextField()
    title = models.CharField(max_length=50)
    pdate = models.DateField(default=timezone.now)  # publication date
    mdate = models.DateField(default=timezone.now)  # modification date

    def __str__(self):
        return self.title


class commments(models.Model):
    article = models.ForeignKey(articlemodel, on_delete=models.CASCADE)
    content = models.TextField()
    cdate = models.DateTimeField(default=timezone.now)
    comname = models.CharField(max_length=50)

    def __str__(self):
        return self.content
