# Generated by Django 4.2.7 on 2023-12-04 08:18

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
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contactNo', models.IntegerField()),
            ],
        ),
    ]
