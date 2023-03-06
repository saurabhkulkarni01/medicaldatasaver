from asyncio.windows_events import NULL
from email.policy import default
from statistics import mode
from django.db import models
from PATIENT.models import *
from .models import *
from COMMON_APP.models import *
from datetime import date
# Create your models here.
from django.contrib.auth.models import User
import datetime

# Create your models here.
def in_30_days():
    return date.today()

class Specialization(models.Model):
	name = models.CharField(max_length=80)

class Disease(models.Model):
	disease = models.CharField(max_length=50)


class DiseaseSpecsRel(models.Model):
	specialization = models.ForeignKey(Specialization,on_delete = models.CASCADE,unique = False, null=True, blank=True, default=NULL)
	disease = models.ForeignKey(Disease,on_delete = models.CASCADE,unique = False, null=True, blank=True, default=NULL)	

class Docter(models.Model):
	name = models.CharField(max_length=40)
	phone = models.IntegerField(unique=False)
	rating = models.FloatField(default=0)
	email = models.EmailField(unique=False)
	gender = models.CharField(max_length=30)
	address = models.CharField(max_length=200)
	age = models.IntegerField(default= 0)
	blood = models.CharField(max_length=10)
	username = models.OneToOneField(User,on_delete = models.CASCADE)
	status = models.BooleanField(default = 0)
	average_fee = models.IntegerField(default=500)
	category = models.CharField(max_length=20)
	specialization = models.ForeignKey(Specialization,on_delete = models.CASCADE,unique = False, null=True, blank=True, default=NULL)
	department = models.CharField(max_length=30 , default = "")
	attendance = models.IntegerField(default = 0)
	salary = models.IntegerField(default = 10000)
	average_appointment_time = models.IntegerField(default=60)

class Blog(models.Model):
	heading = models.TextField()
	blog = models.TextField()
	date = models.DateField()
	views = models.IntegerField()
	doctor = models.ForeignKey(Docter, on_delete = models.CASCADE, null=True, blank=True, default=NULL)
	topic = models.CharField(max_length=50)
	

class Chemist(models.Model):
	shopname = models.TextField()
	ownername = models.TextField()
	phone = models.TextField()
	address = models.TextField()
	rating = models.FloatField(default=0)
	username = models.OneToOneField(User,on_delete = models.CASCADE)



class blocktime(models.Model):
	doctor = models.ForeignKey(Docter,on_delete = models.CASCADE,unique = False)
	starttime = models.TimeField()
	endtime = models.TimeField()
	date = models.DateField(default=in_30_days)
	reason = models.TextField(default="")
	
	def __str__(self):
		return f"{self.starttime.strftime('%d-%m-%Y')}"


class Reviews(models.Model):
	patient = models.ForeignKey(Patient, on_delete = models.CASCADE,unique = True, null=True, blank=True, default=NULL)
	doctor = models.ForeignKey(Docter, on_delete = models.CASCADE,unique = True, null=True, blank=True, default=NULL)
	review = models.TextField()
	rating = models.IntegerField(max_length=2)
	
# Prescription Model
class medreport(models.Model):
	patient = models.ForeignKey(Patient,on_delete = models.CASCADE,unique = False)
	docter = models.ForeignKey(Docter,on_delete = models.CASCADE,unique = False)
	appointment = models.ForeignKey('COMMON_APP.Appointment',on_delete = models.CASCADE,unique = False)

class Prescription2(models.Model):
	prescription = models.CharField(max_length=200)
	symptoms = models.CharField(max_length=200)
	patient = models.ForeignKey(Patient,on_delete = models.CASCADE,unique = False)
	docter = models.ForeignKey(Docter,on_delete = models.CASCADE,unique = False)
	appointment = models.ForeignKey('COMMON_APP.Appointment',on_delete = models.CASCADE,unique = False)
	prescripted_date = models.DateField(auto_now = True) 
	note = models.TextField( blank=True, null=True)
	pulse_rate = models.IntegerField(default=72, blank=True)
	weight = models.IntegerField(default=0, blank=True)
	blood_pressure = models.CharField(max_length=30,default="Normal", blank=True)
	diet = models.TextField()
	



	outstanding = models.IntegerField(default = 0)
	paid = models.IntegerField(default = 0)
	total = models.IntegerField(default = 0)


# HR Dashboard Data