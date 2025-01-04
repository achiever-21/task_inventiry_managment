# Generated by Django 4.2.17 on 2025-01-04 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('staff', 'Staff'), ('user', 'User')], default='user', max_length=10),
        ),
    ]
