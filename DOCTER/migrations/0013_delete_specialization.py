# Generated by Django 4.1.1 on 2022-09-28 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCTER', '0012_remove_docter_specialization'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Specialization',
        ),
    ]