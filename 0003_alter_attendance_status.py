# Generated by Django 5.0.4 on 2024-06-25 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_attendance_date_attendance_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('PRESENT', 'Present'), ('ABSENT', 'Absent'), ('LATE', 'Late'), ('EXCUSED', 'Excused')], default='PRESENT', max_length=20),
        ),
    ]
