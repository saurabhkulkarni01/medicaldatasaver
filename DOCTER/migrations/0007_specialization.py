# Generated by Django 4.1.1 on 2022-09-28 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOCTER', '0006_docter_specialization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
    ]
