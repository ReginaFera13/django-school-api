# Generated by Django 5.0.3 on 2024-03-19 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('student_email', models.CharField(max_length=50)),
                ('personal_email', models.CharField(max_length=50)),
                ('locker_number', models.IntegerField(default=1)),
                ('locker_combination', models.CharField(max_length=50)),
                ('good_student', models.BooleanField(default=True)),
            ],
        ),
    ]
