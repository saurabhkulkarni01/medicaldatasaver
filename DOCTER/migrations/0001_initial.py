# Generated by Django 4.1.1 on 2023-04-04 13:19

import DOCTER.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('COMMON_APP', '0001_initial'),
        ('PATIENT', '0002_patient_dob_patient_allergies_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Docter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone', models.IntegerField()),
                ('rating', models.FloatField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=0)),
                ('blood', models.CharField(max_length=10)),
                ('status', models.BooleanField(default=0)),
                ('average_fee', models.IntegerField(default=500)),
                ('category', models.CharField(max_length=20)),
                ('department', models.CharField(default='', max_length=30)),
                ('attendance', models.IntegerField(default=0)),
                ('salary', models.IntegerField(default=10000)),
                ('average_appointment_time', models.IntegerField(default=60)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.TextField()),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rating', models.IntegerField(max_length=2)),
                ('doctor', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='DOCTER.docter', unique=True)),
                ('patient', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='PATIENT.patient', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.CharField(max_length=200)),
                ('symptoms', models.CharField(max_length=200)),
                ('prescripted_date', models.DateField(auto_now=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('pulse_rate', models.IntegerField(blank=True, default=72)),
                ('weight', models.IntegerField(blank=True, default=0)),
                ('blood_pressure', models.CharField(blank=True, default='Normal', max_length=30)),
                ('diet', models.TextField()),
                ('outstanding', models.IntegerField(default=0)),
                ('paid', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='COMMON_APP.appointment')),
                ('docter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DOCTER.docter')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PATIENT.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Pathologist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.TextField()),
                ('ownername', models.TextField()),
                ('email', models.EmailField(default=0, max_length=254)),
                ('phone', models.TextField()),
                ('address', models.TextField()),
                ('rating', models.FloatField(default=0)),
                ('username', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='medreport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='COMMON_APP.appointment')),
                ('docter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DOCTER.docter')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PATIENT.patient')),
            ],
        ),
        migrations.AddField(
            model_name='docter',
            name='specialization',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='DOCTER.specialization'),
        ),
        migrations.AddField(
            model_name='docter',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DiseaseSpecsRel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='DOCTER.disease')),
                ('specialization', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='DOCTER.specialization')),
            ],
        ),
        migrations.CreateModel(
            name='Chemist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.TextField()),
                ('ownername', models.TextField()),
                ('phone', models.TextField()),
                ('email', models.EmailField(default=0, max_length=254)),
                ('address', models.TextField()),
                ('rating', models.FloatField(default=0)),
                ('username', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('blog', models.TextField()),
                ('date', models.DateField()),
                ('views', models.IntegerField()),
                ('topic', models.CharField(max_length=50)),
                ('doctor', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='DOCTER.docter')),
            ],
        ),
        migrations.CreateModel(
            name='blocktime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('date', models.DateField(default=DOCTER.models.in_30_days)),
                ('reason', models.TextField(default='')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DOCTER.docter')),
            ],
        ),
    ]
