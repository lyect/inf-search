# Generated by Django 4.2.5 on 2023-11-28 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='admission_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='full_name',
            field=models.CharField(max_length=50),
        ),
    ]
