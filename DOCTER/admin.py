from django.contrib import admin

# Register your models here.
from DOCTER.models import *
admin.site.register(Docter)
admin.site.register(Prescription2)
admin.site.register(Specialization)
admin.site.register(Disease)
admin.site.register(DiseaseSpecsRel)
admin.site.register(Blog)
admin.site.register(Pathologist)
admin.site.register(Chemist)
admin.site.register(Test)
admin.site.register(Medicine)
admin.site.register(ChemistMedicine)