from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Receptionist)
admin.site.register(Appointment)
admin.site.register(HR)
admin.site.register(Chat)
admin.site.register(TestAppointment)
admin.site.register(ChemistAppointment)
admin.site.register(MedicineAppointment)

