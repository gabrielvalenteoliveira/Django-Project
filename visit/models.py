from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Users(models.Model):
   nameUser = models.CharField(max_length=30)
   password = models.CharField(max_length=10)
   updatedIn = models.DateTimeField(auto_now=True)

   def __str__(self):
      return f"{self.nameUser} {self.createdIn}"
   
class Register(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   createdIn = models.DateTimeField(auto_now_add=True)
   updatedIn = models.DateTimeField(auto_now=True)

   def __str__(self):
      return f"{self.username}"