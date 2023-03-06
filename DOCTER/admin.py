from django.contrib import admin

# Register your models here.
from DOCTER.models import *
admin.site.register(Docter)
admin.site.register(Prescription2)
admin.site.register(Specialization)
admin.site.register(Disease)
admin.site.register(DiseaseSpecsRel)
admin.site.register(Blog)