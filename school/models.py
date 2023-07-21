from django.db import models
import uuid
# Create your models here.
class Student(models.Model):
    id         = models.UUIDField(default=uuid.uuid4, unique= True, primary_key= True, editable= False)
    firstName  = models.CharField(max_length= 50, null = False, blank= False)
    middelName = models.CharField(max_length= 50, null = False, blank= False)
    lastName   = models.CharField(max_length= 50, null = False, blank= False)
    email      = models.EmailField(max_length= 100, null = False, blank= False)
    age        = models.IntegerField(max_length=3, null = False, blank= False)
    sex        = models.CharField(max_length=1, null = False, blank= False)
    class_room_id = models.ForeignKey()

class Teacher(models.Model):
     id   = models.UUIDField(default=uuid.uuid4, unique= True, primary_key= True, editable= False)
     First_Name = models.CharField(max_length=200, null = False, blank = False)
     Middle_Name = models.CharField(max_length=200, null=True, blank=True)
     Last_Name = models.CharField(max_length=200, null=True, blank=True)
     Date_Of_Birth = models.DateField(max_length=200, null=True, blank=True)
     email = models.EmailField(max_length=200, null=True, blank=True)
     Phone_Number = models.IntegerField(max_length=200, null=True, blank=True)