# Generated by Django 4.1.1 on 2023-02-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOCTER', '0005_alter_blog_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chemist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.TextField()),
                ('ownername', models.TextField()),
                ('phone', models.TextField()),
                ('address', models.TextField()),
                ('rating', models.FloatField(default=0)),
            ],
        ),
    ]