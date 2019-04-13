from django.db import models
from django.contrib.auth.models import  User
from datetime import date
STATUS=[
    ('Absent','Absent'),
    ('Present','Present'),
]
class Person(models.Model):
    name = models.CharField(max_length=10)
    date = models.DateField(("Date"), default=date.today)
    status=models.CharField(max_length=10,choices=STATUS)


    def __str__(self):
        return self.name