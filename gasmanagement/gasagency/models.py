from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Name=models.CharField(max_length=150)
    dob=models.DateField()
    Gen=models.CharField(max_length=15)
    Img=models.ImageField(upload_to='media/')
    Email=models.EmailField(unique=True)
    Pass=models.CharField(max_length=120)
    Cpass=models.CharField(max_length=120)


class Zone(models.Model):
    zone=models.CharField(max_length=150)

    
class Agents(models.Model):
    Name=models.CharField(max_length=125)
    Age=models.IntegerField()
    Licence=models.IntegerField()
    Phone=models.CharField(max_length=10)
    Email=models.EmailField(unique=True)
    Location=models.CharField(max_length=150)
    Joining=models.DateField(auto_now_add=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)



class Cylinder(models.Model):
    Type=models.CharField(max_length=150)
    Price=models.IntegerField()
    Net=models.IntegerField()
    Available=models.IntegerField()

class Feedback(models.Model):
    RATING_CHOICES = [
        (1, "⭐ Poor"),
        (2, "⭐⭐ Fair"),
        (3, "⭐⭐⭐ Good"),
        (4, "⭐⭐⭐⭐ Very Good"),
        (5, "⭐⭐⭐⭐⭐ Excellent"),
    ]
    Date=models.DateField(auto_now_add=True)
    Message=models.CharField(max_length=250)
    Rating=models.IntegerField(choices=RATING_CHOICES)
    customer=models.ForeignKey(Register,on_delete=models.CASCADE)


class Booking(models.Model):
    cylinder=models.ForeignKey(Cylinder,on_delete=models.CASCADE,null=False)
    user=models.ForeignKey(Register,on_delete=models.CASCADE,null=False)
    bookingdate=models.DateField(auto_now_add=True)
    price=models.IntegerField()
    status=models.CharField(max_length=150)

class AssignAgent(models.Model):
    agent=models.ForeignKey(Agents,on_delete=models.CASCADE,null=False,blank=False)
    booking=models.ForeignKey(Booking,on_delete=models.CASCADE,null=False,blank=False)
    status=models.CharField(max_length=20, default="Pending")
    date=models.DateField(auto_now_add=True)
    
    




