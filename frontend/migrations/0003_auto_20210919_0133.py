# Generated by Django 3.2.7 on 2021-09-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_pending_db'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_db',
            name='gender',
            field=models.TextField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pending_db',
            name='notes',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]