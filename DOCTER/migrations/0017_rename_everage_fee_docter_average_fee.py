# Generated by Django 4.1.1 on 2022-10-02 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCTER', '0016_docter_everage_fee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='docter',
            old_name='everage_fee',
            new_name='average_fee',
        ),
    ]