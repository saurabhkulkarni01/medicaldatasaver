from django.db import models


# import in-Built User Models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
	name = models.CharField(max_length=40)
	phone = models.IntegerField(unique=True)
	email = models.EmailField(unique=True)
	gender = models.CharField(max_length=30)
	address = models.CharField(max_length=200)
	age = models.IntegerField(default= 0 )
	blood = models.CharField(max_length=10)
	medical = models.CharField(max_length=100)
	case = models.CharField(max_length=20)
	username = models.OneToOneField(User,on_delete = models.CASCADE)
	health_insurance_no = models.CharField(max_length=15)
	disability = models.CharField(max_length=100)
	DOB = models.DateField( auto_now=True)
	sex = models.CharField(max_length=5)




class Invoice(models.Model):
	patient = models.OneToOneField(Patient,on_delete = models.CASCADE)
	outstanding = models.CharField(max_length =  10)
	paid = models.CharField(max_length = 10)