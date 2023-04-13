from django.contrib import admin
from django.urls import path
from COMMON_APP.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home Page
    path('', home , name = 'home' ),
    path('register', register , name = 'register' ),
    path('login', login , name = 'login' ),
    path('about', about , name = 'about' ),
    path('findSpecs', findSpecs, name = 'findSpecs' ),
    path('appoint/(?P<id>\d+)/$', appoint, name='appoint'),
    path('logout', logout , name = 'logout' ),
    path('profile/(?P<user>.*)/$', profile , name = 'profile' ),
    path('notificaton/(?P<user>.*)/$', notification , name = 'notification' ),
    path('dashboard/(?P<user>.*)/$', dashboard , name = 'dashboard'),
    path('create_appointment/(?P<user>.*)/$', create_appointment , name = 'create_appointment'),
    path('check_availibility/(?P<user>.*)/$', check_availibility , name = 'check_availibility'),
    path('cancel_appoint_pat/(?P<id>\d+)/$', cancel_appoint_pat , name = 'cancel_appoint_pat'),
    path('cancel_appoint_doct/(?P<id>\d+)/$', cancel_appoint_doct , name = 'cancel_appoint_doct'),
    path('block_slot/', block_slot , name = 'block_slot'),
    path('consulting/',consulatation, name="consulting" ),
    path('dietsuggestion/',dietsuggestion , name="dietsuggestion" ),
    path('getdoctorsbydisease',getdoctorbydisease, name='getdoctorbydisease'),
    path('symptomsfinder/',symptomsfinder , name="symptomsfinder" ),
    path('allblogs/(?P<user>.*)/$', allblogs, name = 'allblogs'),
    path('myblog', myblog, name = 'myblog'),
    path('blog/(?P<user>.*)/(?P<id>\d+)/$',  blog, name = 'blog'),
    path('notification/(?P<user>.*)/(?P<id>\d+)/$',  notification, name = 'notification'),
    path('addblog/(?P<user>.*)/$', addblog, name = 'addblog'),
    path('delete_patient/(?P<id>\d+)/$', delete_patient , name = 'delete_patient'),
    path('update_patient/(?P<id>\d+)/$', update_patient , name = 'update_patient'),
    path('patient_history/(?P<id>\d+)/$', med_history , name = 'patient_history'),
    path('doctor_profile/(?P<id>\d+)/$', doctor_profile , name = 'doctor_profile'),
    path('create_patient/', create_patient , name = 'create_patient'),
    path('myappointment/', myappointment , name = 'myappointment'),
    path('mytests/', mytests , name = 'mytests'),
    path('mymedicineorder/', mymedicineorder , name = 'mymedicineorder'),
    path('addmedicine/', addmedicine , name = 'addmedicine'),
    path('docter_appointment/', docter_appointment , name = 'docter_appointment'),
    path('docter_prescription/', docter_prescription , name = 'docter_prescription'),
    path('create_prescription/', create_prescription , name = 'create_prescription'),
    path('medical_history/', medical_history , name = 'medical_history'),
    path('update_status/(?P<id>\d+)/$', update_status , name = 'update_status'),
    path('update_docter/(?P<id>\d+)/$', update_docter , name = 'update_docter'),
    path('delete_docter/', delete_docter , name = 'delete_docter'),
    path('get_pdf/(?P<id>\d+)/$', get_pdf , name = 'get_pdf'),
    path('send_reminder/(?P<id>\d+)/$', send_reminder , name = 'send_reminder'),
    path('create_pathology/',createPathologist, name = 'create_pathology'),
    path('create_chemist/',createChemist, name = 'create_chemist'),
    path('appointment_details/(?P<user>.*)/(?P<id>\d+)/$', appoint_details , name = 'appointment_details'),
    path('create_testappoint/',create_testappoint, name = 'create_testappoint'),
    path('add_pathologist/',add_pathologist, name = 'add_pathologist'),
    path('create_medicineappoint/',create_medicineappoint, name = 'create_medicineappoint'),
    path('add_chemist/',add_chemist, name = 'add_chemist'),
    path('chat/(?P<user>.*)/(?P<id>\d+)/$',chat,name = 'chat'),
    path('addresult/(?P<id>\d+)/$',addresult,name = 'addresult'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)


