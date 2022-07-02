# Generated by Django 3.2.7 on 2021-09-19 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_pending_db2'),
    ]

    operations = [
        migrations.CreateModel(
            name='accepted_db',
            fields=[
                ('reg_id', models.TextField(max_length=20, primary_key=True, serialize=False)),
                ('institute_id', models.TextField(max_length=30, unique=True)),
                ('name', models.TextField(max_length=30)),
                ('dob', models.DateField()),
                ('id_no', models.TextField(max_length=15)),
                ('address', models.TextField(max_length=1000)),
                ('gender', models.TextField(max_length=10, null=True)),
                ('course', models.TextField(max_length=50)),
                ('department', models.TextField(max_length=50)),
                ('specialization', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('file', models.FileField(upload_to='')),
                ('notes', models.TextField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='rejected_db',
            fields=[
                ('reg_id', models.TextField(max_length=20, primary_key=True, serialize=False)),
                ('reason', models.TextField(max_length=1000)),
                ('name', models.TextField(max_length=30)),
                ('dob', models.DateField()),
                ('id_no', models.TextField(max_length=15)),
                ('address', models.TextField(max_length=1000)),
                ('gender', models.TextField(max_length=10, null=True)),
                ('course', models.TextField(max_length=50)),
                ('department', models.TextField(max_length=50)),
                ('specialization', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('file', models.FileField(upload_to='')),
                ('notes', models.TextField(max_length=1000, null=True)),
            ],
        ),
    ]
