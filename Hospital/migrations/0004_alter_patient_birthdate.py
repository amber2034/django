# Generated by Django 4.1.3 on 2022-12-23 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0003_patient_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Birthdate',
            field=models.DateField(default='<jamming-date>', null=True),
        ),
    ]