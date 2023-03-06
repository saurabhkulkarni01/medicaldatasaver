# Generated by Django 4.1.1 on 2023-01-13 11:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DOCTER', '0002_specialization_docter_average_appointment_time_and_more'),
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
            name='DiseaseSpecsRel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='DOCTER.disease')),
                ('specialization', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='DOCTER.specialization')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('blog', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('views', models.IntegerField()),
                ('topic', models.CharField(max_length=50)),
                ('doctor', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='DOCTER.docter', unique=True)),
            ],
        ),
    ]