from django.db import models
from django.contrib.auth.models import User
from DOCTER.models import *
from PATIENT.models import *
# Create your models here.

# Model For Appointment
class Appointment(models.Model):
	docterid = models.ForeignKey('DOCTER.Docter',on_delete = models.CASCADE, default=NULL)
	patientid = models.ForeignKey('PATIENT.Patient',on_delete = models.CASCADE, default=NULL)
	time = models.TimeField()
	date = models.DateField()
	note = models.TextField(max_length=300)
	status = models.BooleanField(max_length = 15, default=0)
	share_permission = models.BooleanField(default=True)
	is_cancelled = models.BooleanField(default=False)
	cancellation_reason = models.TextField(default="")
	cancelled_by_doct = models.BooleanField(default = True)
	is_pop = models.BooleanField (default=False)

class notification(models.Model):
	type = models.IntegerField(default=1)
	message = models.TextField(default="")
	datetime = models.DateTimeField(auto_now=True)
	appointment = models.ForeignKey(Appointment,on_delete = models.CASCADE, default=NULL)
	docterid = models.ForeignKey('DOCTER.Docter',on_delete = models.CASCADE, default=NULL)
	patientid = models.ForeignKey('PATIENT.Patient',on_delete = models.CASCADE, default=NULL)
	blogid = models.ForeignKey(Blog,on_delete = models.CASCADE, default=NULL)
	to_doctor = models.BooleanField(default=False)
	to_patient = models.BooleanField(default=False)



class ChemistAppointment(models.Model):
	status = models.IntegerField(default=0)
	medicinelist = models.TextField()
	appointment = models.ForeignKey(Appointment,on_delete = models.CASCADE, null=True, blank=True, default=NULL)
	chemist = models.ForeignKey(Chemist,on_delete = models.CASCADE, null=True, blank=True, default=NULL)

















































	
# Model For Receptionist
class Receptionist(models.Model):
	name = models.CharField(max_length=40)
	phone = models.CharField(max_length=12,default="",unique=True)
	email = models.CharField(max_length=50,unique=True)
	address = models.CharField(max_length=200)
	username = models.OneToOneField(User,on_delete = models.CASCADE)






# Model For HR
class HR(models.Model):
	name = models.CharField(max_length=40)
	phone = models.CharField(max_length=12,default="",unique=True)
	email = models.CharField(max_length=50,unique=True)
	address = models.CharField(max_length=200)
	username = models.OneToOneField(User,on_delete = models.CASCADE)