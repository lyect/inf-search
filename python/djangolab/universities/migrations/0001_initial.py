# Generated by Django 4.2.5 on 2023-11-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('abbreviation_name', models.CharField(max_length=255)),
                ('founded_date', models.DateField()),
            ],
        ),
    ]