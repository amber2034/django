# Generated by Django 4.1.3 on 2022-12-23 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Symptoms',
            field=models.TextField(default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Date1',
            field=models.DateField(auto_now_add=True),
        ),
    ]