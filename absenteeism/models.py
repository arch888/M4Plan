from django.db import models
from django.contrib.auth.models import  User
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver


STATUS=[
    ('Absent','Absent'),
    ('Present','Present'),
]
choice=[
    ('--select--','--select--'),
    ('Supervisor','Supervisor'),
    ('TeamLeader','TeamLeader'),
    ('Senior Operator','Senior Operator'),
    ('Skilled Operator','Skilled Operator'),
    ('Semi-Skilled Operator','Semi-Skilled Operator'),
    ('Un-Skilled Operator','Un-Skilled Operator'),
    ('Helper','Helper'),
    ('Trainee','Trainee'),
]

SEL=[('LINE-1','LINE-1'),
    ('LINE-2','LINE-2'),
     ('LINE-3','LINE-3'),
     ('LINE-4','LINE-4'),
     ('LINE-5','LINE-5'),
]
class Lining(models.Model):
    select=models.CharField(max_length=10,choices=SEL)

    def __str__(self):
        return str(self.select)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    desig = models.CharField(choices=choice, max_length=20)
    choose=models.ForeignKey(Lining,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)
##
##@receiver(post_save, sender=User)
##def update_user_profile(sender, instance, created, **kwargs):
##    if created:
##        Employee.objects.create(user=instance)
##    instance.employee.save()

    
class Person(models.Model):
    choosen=models.ForeignKey(Lining,on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    date = models.DateField(("Date"), default=date.today)
    status=models.CharField(max_length=10,choices=STATUS)
    
    def __str__(self):
        return self.name + "     "+ str(self.date)+"      " +self.status
