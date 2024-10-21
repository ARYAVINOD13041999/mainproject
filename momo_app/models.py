from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)


class customer(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='customer')

    name = models.CharField(max_length=100)
    email = models.EmailField()
    Address = models.TextField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class worker(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='worker')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    Address = models.TextField()
    phone = models.CharField(max_length=10)

class complaint(models.Model):
    user = models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    replay = models.CharField(null=True,blank=True,max_length=100)


class add(models.Model):
    notification = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)

class schedule(models.Model):
    date =  models.DateField()
    startingtime = models.TimeField()
    endingtime= models.TimeField()

    # def __str__(self):
    #     return self.date



class appointment(models.Model):
    appointment = models.ForeignKey(customer,on_delete=models.CASCADE,name='appointment')
    schedule = models.ForeignKey(schedule,on_delete = models.CASCADE)
    status = models.IntegerField(default = 0)








