from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class institute_db(models.Model):
    reg_id=models.TextField(max_length=10,primary_key=True)
    name=models.CharField(max_length=30)


class pending_db(models.Model):
    name=models.TextField(max_length=30)
    dob=models.DateField()
    id_no=models.TextField(max_length=15)
    address=models.TextField(max_length=1000)
    gender=models.TextField(max_length=10,null=True)
    course=models.TextField(max_length=50)
    department=models.TextField(max_length=50)
    specialization=models.TextField(max_length=100)
    image=models.ImageField()
    file=models.FileField()
    notes=models.TextField(max_length=1000,null=True)
    
    


class pending_db2(models.Model):
    reg_id=models.TextField(max_length=20)
    name=models.TextField(max_length=30)
    dob=models.DateField()
    id_no=models.TextField(max_length=15)
    address=models.TextField(max_length=1000)
    gender=models.TextField(max_length=10,null=True)
    course=models.TextField(max_length=50)
    department=models.TextField(max_length=50)
    specialization=models.TextField(max_length=100)
    image=models.ImageField()
    file=models.FileField()
    notes=models.TextField(max_length=1000,null=True)


class pending_db1(models.Model):
    reg_id=models.TextField(max_length=20,primary_key=True)
    name=models.TextField(max_length=30)
    dob=models.DateField()
    id_no=models.TextField(max_length=15)
    address=models.TextField(max_length=1000)
    gender=models.TextField(max_length=10,null=True)
    course=models.TextField(max_length=50)
    department=models.TextField(max_length=50)
    specialization=models.TextField(max_length=100)
    image=models.ImageField()
    file=models.FileField()
    notes=models.TextField(max_length=1000,null=True)



class accepted_db(models.Model):
    reg_id=models.TextField(max_length=20,primary_key=True)
    institute_id=models.TextField(max_length=30,unique=True)
    name=models.TextField(max_length=30)
    dob=models.DateField()
    id_no=models.TextField(max_length=15)
    address=models.TextField(max_length=1000)
    gender=models.TextField(max_length=10,null=True)
    course=models.TextField(max_length=50)
    department=models.TextField(max_length=50)
    specialization=models.TextField(max_length=100)
    image=models.ImageField()
    file=models.FileField()
    notes=models.TextField(max_length=1000,null=True)



class rejected_db(models.Model):
    reg_id=models.TextField(max_length=20,primary_key=True)
    reason=models.TextField(max_length=1000)
    name=models.TextField(max_length=30)
    dob=models.DateField()
    id_no=models.TextField(max_length=15)
    address=models.TextField(max_length=1000)
    gender=models.TextField(max_length=10,null=True)
    course=models.TextField(max_length=50)
    department=models.TextField(max_length=50)
    specialization=models.TextField(max_length=100)
    image=models.ImageField()
    file=models.FileField()
    notes=models.TextField(max_length=1000,null=True)

    
    
        
    
    