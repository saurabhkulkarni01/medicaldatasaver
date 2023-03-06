from datetime import date, timedelta
from sqlite3 import Time
from django.shortcuts import render , redirect , HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import View
from django import template
from django.template.loader import get_template
from io import BytesIO
import xhtml2pdf.pisa as pisa
from .utils import render_to_pdf #created in step 4
from django.db import IntegrityError
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from DOCTER.models import *
from PATIENT.models import *
from COMMON_APP.models import *
from Application_Main.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from datetime import date
from datetime import time
import datetime
from .sms import *
from .chatgpt import getans
from .whatsappsms import welcomemsg
from .mail import welcomemail
# Create your views here.
def home(request):
	specs = Specialization.objects.all()
	disease = Disease.objects.all()
	return render(request , 'home.html',{"user":None , "specs":specs, "disease": disease})

def register(request) :
	specs = Specialization.objects.all()
	disease = Disease.objects.all()
	if request.method == 'POST':
		print(type(request.POST['name']),type(request.POST['phone']))
		print(request.POST['post'])
		
		# try:
		# 	SendWelcomeMessage(name=request.POST['name'],phone=request.POST['phone'])
		# except:
		# 	pass
		
		# welcomemsg()
		welcomemail()
		
		try:
			user = User.objects.get(username=request.POST['username'])
			print(user)
			return render(request,'register.html')
		except User.DoesNotExist:
			user = User.objects.create_user(username=request.POST['username'],password=request.POST['pass1'])
			if request.POST['post'] == 'Patient':
				new = Patient(phone=request.POST['phone'],name=request.POST['name'],email=request.POST['email'],username=user)	
				new.save()	

				c_patient = Invoice(patient = new , outstanding = 0 , paid = 0)
				c_patient.save()

				return render(request , 'home.html',{"user":None, "specs":specs})
			else:
				specsid = request.POST['specs']
				spec= Specialization.objects.get(name=specsid)
				new = Docter(phone=request.POST['phone'],name=request.POST['name'],email=request.POST['email'],username=user, specialization=spec)	
				new.save()	
				print(new)
				return render(request , 'home.html',{"user":None, "specs":specs,"disease":disease})
	
			print('Registered Successfully')
			return render(request,'register.html')
	else:
			specs = Specialization.objects.all()
			return render(request,'register.html',{"specs": specs})


# Login
def login(request):
	specs = Specialization.objects.all()
	if request.method == 'POST':
		# getans("is chatgpt working")
		try:
 			# Check User in DB
	 		
			pwd = request.POST['pass1']
			uname = request.POST['username']
	 		
			user_authenticate = auth.authenticate(username=uname,password=pwd)
			
			if user_authenticate != None:
				user = User.objects.get(username=uname)
				try:
					data = Patient.objects.get(username = user)
					print(data)
					print('Patient has been Logged')
					auth.login(request,user_authenticate)				
					return redirect('dashboard',user= "P")
				except:
					try:
						data = Docter.objects.get(username = user )
						auth.login(request,user_authenticate)				
						print('Docter has been Logged')
						return redirect('dashboard',user = "D")	 					
					except:
						return redirect('/')			
			else:
				print('Login Failed')
				return render(request,'error.html',{"msg":"Wrong Username or password !"})
		except:
			return render(request,'error.html',{"msg":"Wrong Username or password !"})
	return render(request , 'login.html',{"specs":specs})

# Logout
def logout(request):
	# welcomemail()
	auth.logout(request)
	print('Logout')
	return redirect('/login')


def findSpecs(request):
	specs = Specialization.objects.all()
	if request.method == "POST":
		spcname = request.POST['specs']
		specialization = Specialization.objects.get(name = spcname)
		doctors = Docter.objects.filter( specialization = specialization )
		# print(spcname, doctors)
		return render(request,'doctorlist.html',{"user" : "P", "doctors": doctors, "specialization": specialization,"status":True})
		# return render(request,'register.html',specs=specs)
	return redirect('/')

# Profile
def profile(request, user):
	print(request.user)
	userid = User.objects.get(username=request.user)
	status = False
	if request.user:
		status = request.user
	if request.method == "POST":
		print(request.POST['name'])
		if user == "P":
			update = Patient.objects.get(username=userid)
			update.name = request.POST['name']
			update.phone = request.POST['phone']
			update.email = request.POST['email']
			update.gender = request.POST['gender']
			update.age = request.POST['age']
			update.blood = request.POST['blood']
			update.address = request.POST['address']
			update.health_insurance_no = request.POST['health_insurance_no']
			update.disability = request.POST['disability']
			update.DOB = request.POST['DOB']
			try:
				update.case = request.POST['case']
			except:
				update.case = ""
			try:
				myfile = request.FILES['report']
				fs = FileSystemStorage(location='media/report/')
				filename = fs.save(myfile.name,myfile)
			# print(name,file)
				url = fs.url(filename)
				print(url)
				update.medical = url
			except:
				pass
			update.save()
			return redirect('dashboard',user = user)
		if user == "D":
			update = Docter.objects.get(username=userid)
			update.name = request.POST['name']
			update.average_fee = request.POST['average_fee']
			update.average_appointment_time = request.POST['average_appointment_time']
			update.phone = request.POST['phone']
			update.email = request.POST['email']
			update.gender = request.POST['gender']
			update.age = request.POST['age']
			update.blood = request.POST['blood']
			update.address = request.POST['address']
			update.save()
			return redirect('dashboard',user = user)
		if user == "C":
			update = Chemist.objects.get(username=userid)
			update.name = request.POST['name']
			update.shop_name = request.POST['shop_name']
			update.average_appointment_time = request.POST['average_appointment_time']
			update.phone = request.POST['phone']
			update.email = request.POST['email']
			update.gender = request.POST['gender']
			update.age = request.POST['age']
			update.blood = request.POST['blood']
			update.address = request.POST['address']
			update.save()
			return redirect('dashboard',user = user)




	if user == "P":
		userdata = Patient.objects.get(username=userid)
		return render(request  , 'patient_profile.html',{'userdata' : userdata , 'user':user, "status": status})

	else:
		userdata  = Docter.objects.get(username=userid)
		return render(request  , 'docter_profile.html',{'userdata' : userdata , 'user':user, "status": status})


	return redirect('/')



def dashboard(request , user):
	print(user)
	disease = Disease.objects.all()
	specs= Specialization.objects.all()
	status = False
	if request.user:
		status = request.user
	if user == "AnonymousUser":
		return redirect('home')
	
	return render(request , 'home.html', {'user':user, "status": status, "specs":specs,"disease":disease})

def is_available(doctor , appoint_date, tim):
	f=0
	avg_time = doctor.average_appointment_time
	min = tim.minute + avg_time
	hours = tim.hour
	hours += int(min/60)
	min = min%60
	endtime = time(hours,min,0)
	
	timm = time(tim.hour, tim.minute,0)
	tim= timm
	# print(blocktime.objects.filter(date=appoint_date, doctor=doctor)[0].starttime,blocktime.objects.filter(date=appoint_date, doctor=doctor)[0].endtime,111111111111111)
	# print(type(tim))
	print(tim,endtime)
	tmappointment = Appointment.objects.filter(date=appoint_date, docterid=doctor, time__gte = tim , time__lt =endtime, is_cancelled=False)
	if len(tmappointment)>0 :
		f=1
	tblock = blocktime.objects.filter(date=appoint_date, doctor=doctor, starttime__gte = tim , starttime__lt =endtime)
	if len(tblock)>0 :
		f=1
	tblock = blocktime.objects.filter(date=appoint_date, doctor=doctor, endtime__gte = tim , endtime__lte =endtime)
	if len(tblock)>0 :
		f=1
	tblock = blocktime.objects.filter(date=appoint_date, doctor=doctor, endtime__gte = endtime , starttime__lte = tim )
	# print(tim, endtime,f,tblock)
	if len(tblock)>0 :
		f=1
	tblock = blocktime.objects.filter(date=appoint_date, doctor=doctor, endtime__lte = endtime , starttime__gte = tim )
	if len(tblock)>0 :
		f=1
	return f


def create_appointment(request , user):
	userid = User.objects.get(username=request.user)
	status = False
	specs= Specialization.objects.all()
	disease = Disease.objects.all()
	if request.user:
		status = request.user

	if request.method == "POST":
		
		d_id = int(request.POST['docter'])
		p_id = int(request.POST['patient'])
		id_user = User.objects.get(pk=p_id)
		docter = Docter.objects.get(pk=d_id)
		patient = Patient.objects.get(username=userid)
		
		print(d_id, type(d_id),p_id,patient)
		p_id = int(request.POST['patient'])
		status = int(request.POST['status'])
		try:
			share_permission=bool(request.POST['share_data'])

		except:
			share_permission = False
		appoint_date = datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d")
		today_date = datetime.datetime.today()
		print(request.POST['time'],type(request.POST['time']))
		if appoint_date <= today_date :
			patient_names = Patient.objects.all()
			docter_names = Docter.objects.all()	
			return render(request,'error.html',{"msg":"Select Valid Date and Time",'user':user,'puser':userid, "status": status})
			return redirect( 'create_appointment' , {'user':user,'puser':userid, "status": status , "patient_names" : patient_names , 
				"docter_names" : docter_names,"share_permission":share_permission })
		print(request.POST['time'],type(request.POST['time']))
		f = is_available(docter,appoint_date,datetime.datetime.strptime(request.POST['time'], "%H:%M"))
		print(f,111)
		if f==1 :
			patient_names = Patient.objects.all()
			docter_names = Docter.objects.all()	
			return render(request , 'home.html' ,{"msg":"Appointment Not created! Select another date or Time ",'user':'P','puser':userid, "status": True , "patient_names" : patient_names , 
	"docter_names" : docter_names,'specs':specs,"disease":disease})
		
		try:
			appointmentbooked(name=docter.name,phone=docter.phone, withname=patient.name, date=request.POST['date'])
			appointmentbooked(withname=docter.name,phone=patient.phone, name=patient.name, date=request.POST['date'])
		except:
			pass

		new_appointment = Appointment(docterid = docter , patientid = patient ,time = request.POST['time'] ,  date = request.POST['date'] , status  = status, share_permission = share_permission )
		new_appointment.save()
		print(new_appointment,new_appointment.patientid)
		return redirect('dashboard',user = user)

    
	patient_names = Patient.objects.all()
	docter_names = Docter.objects.all()	

	return render(request , 'create_appointment.html' , {'user':user,'puser':userid, "status": status , "patient_names" : patient_names , 
		"docter_names" : docter_names })




# Delete Patient
def delete_patient(request , id ):
	data = Patient.objects.get(id=id)
	data.delete()
	return redirect('receptionist_dashboard' , user="R")



# Create Patient => Receptionist
def create_patient(request):
	status = False
	specs = Specialization.objects.all()
	if request.user:
		status = request.user
	if request.method =="POST":
		try:
			user = User.objects.get(username=request.POST['username'])
			print(user)
			return redirect('receptionist_dashboard', user = "R")
		except User.DoesNotExist:

			user = User.objects.create_user(username=request.POST['username'],password='default')	
			try:
				myfile = request.FILES['report']
				fs = FileSystemStorage(location='media/report/')
				filename = fs.save(myfile.name,myfile)
			# print(name,file)
				url = fs.url(filename)
				
			except:
				url = ""		
			new = Patient(phone=request.POST['phone'],name=request.POST['name'],email=request.POST['email'],username=user,age=request.POST['age'] ,address = request.POST['address'] , gender =  request.POST['gender'] , blood = request.POST['blood'] , case = request.POST['case'] , medical = url)	
			new.save()	

			c_patient = Invoice(patient = new , outstanding = request.POST['outstanding'] , paid = request.POST['paid'])
			c_patient.save()
			return render(request , 'home.html', {'user':user, "status": status, "specs":specs})
			

	return render(request , 'home.html', {'user':user, "status": status})



# Update Patient=> Receptionist
def update_patient(request , id ):
	status = False
	if request.user:
		status = request.user
	if request.method == "POST":
			update = Patient.objects.get(id=id)
			update.name = request.POST['name']
			update.phone = request.POST['phone']
			update.email = request.POST['email']
			update.gender = request.POST['gender']
			update.age = request.POST['age']
			update.blood = request.POST['blood']
			update.address = request.POST['address']
			update.case = request.POST['case']
			try:
				myfile = request.FILES['report']
				fs = FileSystemStorage(location='media/report/')
				filename = fs.save(myfile.name,myfile)
			# print(name,file)
				url = fs.url(filename)
				print(url)
				update.medical = url
			except:
				pass
			update.save()
			extra_update = Invoice.objects.get(patient = update)

			extra_update.outstanding = request.POST['outstanding']
			extra_update.paid = request.POST['paid']
			extra_update.save()
			return redirect('receptionist_dashboard' , user = "R")
	data = Patient.objects.get(id=id)
	extra = Invoice.objects.get(patient = data)
	return render(request , 'update_patient.html' , {'data':data , 'extra':extra , 'user' :"R" , 'status':status})


def myappointment(request):
	status = False
	if request.user:
		status = request.user
	user_id = User.objects.get(username=request.user)
	patient= Patient.objects.get(username=user_id)
	data = Appointment.objects.filter(patientid=patient)
	for appoint in data:
		appoint.is_pop = False
		appoint.save() 
	return render(request , 'my_appointment.html' , {'data':data, 'user' :"P" , 'status':status})


# Docter Appointsments

def docter_appointment(request):
	status = False
	if request.user:
		status = request.user
	user_id = User.objects.get(username=request.user)
	docter= Docter.objects.get(username=user_id)
	data = Appointment.objects.filter(docterid=docter)
	for appoint in data:
		appoint.is_pop = False
		appoint.save()
	return render(request , 'my_appointment.html' , {'data':data, 'user' :"D" , 'status':status})


# Docter Prescription

def docter_prescription(request):
	status = False
	if request.user:
		status = request.user
	user_id = User.objects.get(username=request.user)
	docter = Docter.objects.get(username=user_id)
	print(docter,user_id)
	pers   = Prescription2.objects.filter(docter = docter)
	print(len(pers))
	for i in pers:
		print(i.patient)
	return render(request , 'docter_prescription.html' , {'pers':pers, 'user' :"D" , 'status':status})



# Create Prescription 
def create_prescription(request):
	status = False
	if request.user:
		status = request.user
	if request.method == 'POST':

		appointment = Appointment.objects.get(id=request.POST['appointment'])
		
		user_id = User.objects.get(username=request.user)
		docter = Docter.objects.get(username=user_id)
		new_prescrition = Prescription2(symptoms = request.POST['symptoms'] , prescription = request.POST['prescription'] , patient = appointment.patientid , docter = docter , appointment = appointment)
		new_prescrition.save()
		return redirect('docter_prescription')
	user_id = User.objects.get(username=request.user)
	docter = Docter.objects.get(username=user_id)
	data = Appointment.objects.filter(docterid=docter,status=True )
	print(data)

	return render(request , 'create_prescription.html',{"data":data , 'user' : "D" , 'status' : status})


# Mediacal History

def medical_history(request):
	status = False
	if request.user:
		status = request.user
	user_id = User.objects.get(username=request.user)
	print(user_id)
	patient = Patient.objects.get(username = user_id)
	data = Prescription2.objects.filter(patient = patient)
	print(data)
	return render(request , 'medical_history.html',{"data":data , 'user' : "P" , 'status' : status})

def med_history(request , id):
	# userid = User.objects.get(id=id)
	# print(userid,id)
	status = False
	if request.user:
		status = request.user
	patient = Patient.objects.get(id=id)
	data = Prescription2.objects.filter(patient=patient).order_by('-prescripted_date')
	print(patient,data)
	return render(request , 'Patient_History.html',{"data":data , 'user' : "D" , 'status' : status, 'patient':patient})

def doctor_profile(request , id):
	status = True
	if request.user:
		status = request.user
	doctor = Docter.objects.get(id=id)
	review = Reviews.objects.filter(doctor = doctor)
	blogs = Blog.objects.filter(doctor = doctor)
	userid = User.objects.get(username=request.user)
	return render(request , 'specialized_doctor_profile.html',{"review":review , 'user' : "P" , 'status' : status, 'doctor':doctor, 'puser':userid, 'blogs':blogs})

def check_availibility(request , user):
	userid = User.objects.get(username=request.user)
	status = False
	if request.user:
		status = request.user

	if request.method == "POST":
		
		d_id = int(request.POST['docter']) 
		docter = Docter.objects.get(pk=d_id) 
		appoint_date = datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d") 
		availibility = []
		appoints = Appointment.objects.filter(date=appoint_date, docterid=d_id)
		for  app in appoints :
			print(app.time)
		average_appointment_time = docter.average_appointment_time
		aveg_hr = int(average_appointment_time/60) 
		aveg_min = average_appointment_time%60
		print(aveg_hr, aveg_min, type(aveg_min), type(aveg_hr))
		starttime = time(10,0)
		endtime = time(21,00)
		avail_date=appoint_date.date
		delta = timedelta(hours=1)
		st = time(10,0)
		nxt =time(st.hour+aveg_hr ,st.minute+aveg_min)
		while st <= endtime:
			
			f=0
			tmappointment = Appointment.objects.filter(date=appoint_date, docterid=d_id, time__gte = st , time__lt =nxt, is_cancelled=False)
			if len(tmappointment)>0 :
				f=1
			tblock = blocktime.objects.filter(date=appoint_date, doctor=d_id, starttime__gte = st , starttime__lt =nxt)
			if len(tblock)>0 :
				f=1
			tblock = blocktime.objects.filter(date=appoint_date, doctor=d_id, endtime__gte = st , endtime__lte =nxt)
			if len(tblock)>0 :
				f=1
			tblock = blocktime.objects.filter(date=appoint_date, doctor=d_id, endtime__gte = nxt , starttime__lte =st)
			if len(tblock)>0 :
				f=1
			availibility.append({
				"f":f,
				"start":st.hour,
				"start_min":  st.minute,
				"end":nxt.hour,
				"end_min": nxt.minute
			})
			st=nxt
			addmin=st.minute+aveg_min
			addhr= aveg_hr+ int(addmin/60)
			addmin=addmin%60
			nxt =time(st.hour+addhr ,addmin)
		doctor = Docter.objects.get(id=d_id)
		blogs = Blog.objects.filter(doctor = doctor)
		review = Reviews.objects.filter(doctor = doctor)
		userid = User.objects.get(username=request.user)
		return render(request , 'specialized_doctor_profile.html',{"avail_date":avail_date , "availibility":availibility, "review":review , 'user' : "P" , 'status' : status, 'doctor':doctor, 'puser':userid, 'blogs':blogs})
			 

	doctor = Docter.objects.get(id=id)
	blogs = Blog.objects.filter(doctor = doctor)
	review = Reviews.objects.filter(doctor = doctor)
	userid = User.objects.get(username=request.user)
	return render(request , 'specialized_doctor_profile.html',{"review":review , 'user' : "P" , 'status' : status, 'doctor':doctor, 'puser':userid, 'blogs':blogs})

def appoint(request, id):
	status = True
	if request.user:
		status = request.user
	appointment = Appointment.objects.get(id=id)
	prescription = Prescription2.objects.filter(appointment = appointment) 
	userid = User.objects.get(username=request.user)
	return render(request , 'appoint.html',{"appointment":appointment, 'user' : "D" , 'status' : status, 'prescription':prescription, 'puser':userid})

def cancel_appoint_doct( request , id):
	status = True
	if request.user :
		status = request.user
	if request.method == "POST":
		try :
			appoint = Appointment.objects.get(id=id)
			appoint.is_cancelled=True
			appoint.cancelled_by_doct = True
			appoint.is_pop=True
			reason = request.POST['reason']
			appoint.cancellation_reason = reason
			appoint.save()
		except:
			pass
		user_id = User.objects.get(username=request.user)
		docter= Docter.objects.get(username=user_id)
		data = Appointment.objects.filter(docterid=docter)
		try:
			appointmentcancellation(name=docter.name,phone=docter.phone, withname=appoint.patientid.name, date=appoint.date, reason=reason)
			appointmentcancellation(withname=docter.name,phone=appoint.patientid.phone, name=appoint.patientid.name, date=appoint.date, reason=reason)
		except:
			pass
		# try :
		# 	appoint = Appointment.objects.get(id=id)
		# 	appoint.is_pop= False
		# 	appoint.save()
		# except : 
		# 	pass

		return render(request , 'my_appointment.html' , {'data':data, 'user' :"D" , 'status':status})
	appointment = Appointment.objects.get(id=id)
	user_id = User.objects.get(username=request.user)
	docter= Docter.objects.get(username=user_id)
	data = Appointment.objects.filter(docterid=docter)
	return render(request , 'cancel_appoint.html' , {'data':data, 'user' :"D" , 'status':status, 'appointment':appointment})

def cancel_blockslot_appoint(blockslot):
	date = blockslot.date
	starttime = blockslot.starttime
	endtime = blockslot.endtime
	doctor = blockslot.doctor 
	tmappointment = Appointment.objects.filter(date=date, docterid=doctor, time__gte = starttime , time__lte =endtime, is_cancelled=False)
	for appoint in tmappointment:
		appoint.is_cancelled=True
		appoint.cancelled_by_doct = True
		appoint.cancellation_reason = "Slot not available"
		appoint.is_pop=True
		appoint.save()
	return

def block_slot(request):
	
	if request.method == "POST":
		reason = request.POST['reason']
		starttime = request.POST['starttime']
		endtime = request.POST['endtime']
		user_id = User.objects.get(username=request.user)
		doctor = Docter.objects.get(username=user_id)
		date = request.POST['date']
		new_block = blocktime(doctor=doctor, date=date ,reason=reason , starttime=starttime, endtime=endtime)
		new_block.save()
		cancel_blockslot_appoint(new_block)
		allblocks = blocktime.objects.filter(doctor=doctor)
		print(allblocks)
		# print(spcname, doctors)
		return render(request, 'blocktimelist.html',{'data':allblocks, 'user' :"D" , 'status':True, 'doctor':doctor}) 
	user_id = User.objects.get(username=request.user)
	doctor = Docter.objects.get(username=user_id)

	allblocks = blocktime.objects.filter(doctor=doctor)
	print(doctor, allblocks)
		# return render(request,'register.html',specs=specs)
	# return redirect('/')
	return render(request, 'blocktimelist.html',{'data':allblocks, 'user' :"D" , 'status':True, 'doctor':doctor}) 

def cancel_appoint_pat( request , id):
	status = True
	if request.user :
		status = request.user
	if request.method == "POST":
		try :
			appoint = Appointment.objects.get(id=id)
			appoint.is_cancelled=True
			appoint.cancelled_by_doct = False
			appoint.is_pop=True
			reason = request.POST['reason']
			appoint.cancellation_reason = reason
			appoint.save()
		except:
			pass
		user_id = User.objects.get(username=request.user)
		pat= Patient.objects.get(username=user_id)
		data = Appointment.objects.filter(patientid=pat)
		# try :
		# 	appoint = Appointment.objects.get(id=id)
		# 	appoint.is_pop= False
		# 	appoint.save()
		# except : 
		# 	pass

		return render(request , 'my_appointment.html' , {'data':data, 'user' :"P" , 'status':status})
	
	user_id = User.objects.get(username=request.user)
	appointment = Appointment.objects.get(id=id)
	pat= Patient.objects.get(username=user_id)
	data = Appointment.objects.filter(patientid=pat)
	return render(request , 'cancel_appoint.html' , {'data':data, 'user' :"P" , 'status':status, 'appointment':appointment})

def allblogs(request,user):
	allblogs = Blog.objects.all().order_by('date').reverse()
	
	return render(request , 'blogs.html' , {'allblogs':allblogs, 'user' :user , 'status':True} )

def blog(request, user,id):
	status = False
	if request.user:
		status = request.user
	blog = Blog.objects.get(id=id)
	blog.views = blog.views + 1
	blog.save()
	return render(request , 'blog.html' , {'blog':blog, 'user' :user , 'status':True} ) 

def notification(request, user,id):
	status = False
	if request.user:
		status = request.user
	blog = Blog.objects.get(id=id)
	blog.views = blog.views + 1
	blog.save()
	return render(request , 'blog.html' , {'blog':blog, 'user' :user , 'status':True} ) 

def myblog(request):
	duser = request.user
	doctor = Docter.objects.get(username=duser)
	allblogs = Blog.objects.filter(doctor=doctor)
	return render(request , 'blogs.html' , {'allblogs':allblogs, 'user' :"D" , 'status':True} )

def addblog(request, user):
	print(request.user)
	status = False
	if request.user:
		status = request.user
	if request.method == "POST":
		
		# try :
		
		duser = request.user
		
		doctor = Docter.objects.get(username=duser)
		print(doctor)  
		date = datetime.date.today()
		heading = request.POST['heading']
		blog = request.POST['blog']
		topic = request.POST['topic']
		views = 0
		print(1)
		new_blog = Blog(doctor = doctor , heading=heading ,  date = date , blog  = blog, topic=topic, views = views)
		new_blog.save()
		# except:
		# 	pass
		allblogs = Blog.objects.all() 
	
		return render(request , 'blogs.html' , {'allblogs':allblogs, 'user' :user , 'status':True} )
	return render(request , 'addblog.html' , { 'user' :user , 'status':True, 'doctor':request.user} ) 

def consulatation(request): 
	specs = Specialization.objects.all()
	if request.user:
		status = request.user
	if request.method == "POST":
		query = request.POST['query']
		ans = getans(query=query)
		return render(request, 'consulting.html',{"status":status,"query":query,"ans":ans,'user':"P","specs":specs})	
	
	return render(request, 'consulting.html',{"status":status,'user':"P","specs":specs})

def dietsuggestion(request): 
	specs = Specialization.objects.all()
	if request.user:
		status = request.user
	if request.method == "POST":
		age = request.POST['Age']
		weight = request.POST['Weight']
		height = request.POST['Height']
		query = "Suggest a diet for indian with age "+age+" height "+ height + "cm and weight "+weight+" kg"
		ans = getans(query=query)
		return render(request, 'diet_suggestion.html',{"status":status,"query":query,"ans":ans,'user':"P","specs":specs})	
	
	return render(request, 'diet_suggestion.html',{"status":status,'user':"P","specs":specs})

def notification(request,user):
	specs = Specialization.objects.all()
	if request.user:
		status = request.user
	return render(request,'notification.html',{"status":status,"user":user})

def getdoctorbydisease(request):
	specs = Specialization.objects.all()
	if request.user:
		status = request.user
	if request.method == "POST":
		diseases = request.POST['disease']
		diseas = Disease.objects.get(disease = diseases)
		print(diseas)
		rels = DiseaseSpecsRel.objects.filter(disease=diseas)
		doctor =  Docter.objects.filter(name="zinmsnjbdjbnnkndek")
		for rel in rels:
			doctor = doctor | Docter.objects.filter(specialization=rel.specialization)
		return render(request,'doctorlist.html',{"user" : "P", "doctors": doctor ,"status":True})
		pass
	return

def symptomsfinder(request): 
	specs = Specialization.objects.all()
	if request.user:
		status = request.user
	if request.method == "POST":
		query = request.POST['query']
		ans = getans(query=query)
		return render(request, 'consulting.html',{"status":status,"query":query,"ans":ans,'user':"P","specs":specs})	
	
	return render(request, 'consulting.html',{"status":status,'user':"P","specs":specs})
# Upadate Status
def update_status(request  , id):
	print(id)
	specs = Specialization.objects.all()
	status = False
	if request.user:
		status = request.user
	
	data  = Appointment.objects.get(id = id)
	try:
		pers = Prescription2.objects.get(appointment = data)
		pers.outstanding =  0
		pers.paid = 0
		pers.total = 0
		pers.save()
	except:
		print()
	data.status = 1
	data.save()
	return render(request, 'home.html',{"status":status,'user':"D","specs":specs})



	# => Docter Update
def update_docter(request , id):
	status = False
	specs = Specialization.objects.all()
	if request.user:
		status = request.user
	if request.method == "POST":
		update = Docter.objects.get(id=id)
		update.name = request.POST['name']
		update.phone = request.POST['phone']
		update.email = request.POST['email']
		update.gender = request.POST['gender']
		update.age = request.POST['age']
		update.blood = request.POST['blood']
		update.address = request.POST['address']
		update.department = request.POST['department']
		update.salary = request.POST['salary']
		update.status = request.POST['status']
		update.attendance = request.POST['attendance']
		update.save()
		return redirect('home', {"specs":specs})
	data = Docter.objects.get(id= id)
	return render(request , 'update_docter.html' , {"userdata" : data , 'user' : "H" , 'status' : status})



# Docter Delete
def delete_docter(request):
	return HttpResponse('<h2 style="color:red">You are Not authorized</h2>')



# HR Accounting



# Patient invoice 
def patient_invoice(request):
	status = False
	if request.user:
		status = request.user
	user_id =  User.objects.get(username = request.user)
	p = Patient.objects.get(username = user_id)
	data = Prescription2.objects.filter(patient = p)
	return render(request , 'patient_invoice.html' , {'data':data , 'user' : 'P' , 'status' : status})




# About 
def about(request):
	status = False
	specs = Specialization.objects.all()
	if request.user:
		status = request.user
	return render(request , 'about.html' , {"specs":specs})




#  Invoice Generator
def get_pdf(request , id):
	data = Prescription2.objects.get(id=id)
	pdf_data = {'data':data}
	template = get_template('invoice.html')
	data_p = template.render(pdf_data)
	response = BytesIO()
	pdf_page = pisa.pisaDocument(BytesIO(data_p.encode('UTF_8')),response)
	if not pdf_page.err:
		return HttpResponse(response.getvalue(),content_type = 'application/pdf')
	else:
		return HttpResponse('Error')




# Send Reminder
def send_reminder(request,id):
	p = Prescription2.objects.get(id=id)
	email = p.patient.email
	subject = 'Payment Reminder '
	message = 'Your Due Amount is {} outstanding and {} rs. you have already paid'.format(p.outstanding,p.paid)
	recepient = [email]
	send_mail(subject, message, EMAIL_HOST_USER, recepient, fail_silently = False)
	return redirect('hr_accounting')
