# Generated by Django 5.0.1 on 2024-01-20 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeMaster', '0002_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.AlterField(
            model_name='student',
            name='contactNo',
            field=models.IntegerField(max_length=20),
        ),
    ]
