# Generated by Django 3.2.8 on 2022-10-09 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=20)),
                ('emp_designation', models.CharField(max_length=20)),
                ('emp_salary', models.CharField(max_length=20)),
                ('emp_address', models.CharField(max_length=20)),
            ],
        ),
    ]