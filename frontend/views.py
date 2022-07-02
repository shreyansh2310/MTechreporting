from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth #this will be used to authenticate the entered data and will also used to store data in the databse
from django.contrib import messages
from django.db import models
from .models import accepted_db, institute_db, pending_db1, pending_db2
import random
# Create your views here.

def home(request):
    # return HttpResponse('<h1>This is your home page</h1>') this is to return static lines
    return render(request,'frontend/home.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.warning(request,'you are logged in successfully')
            return redirect('dashboard')
            # return render(request,'frontend/home.html')
            
        else:
            messages.warning(request,'Invalid Credentials')
            return render(request,'frontend/admin-signup.html')
        
    return render(request,'frontend/student_login.html')


def signup(request):
    if request.method=='POST':
        print("request method is post")
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            print("password matched")
            if User.objects.filter(email=email).exists():
                messages.warning(request,'Email Already Used')
                return render(request,'frontend/admin-signup.html')
            elif User.objects.filter(username=username).exists():
                
                messages.warning(request,'Username Already Exists')
                return render(request,'frontend/admin-signup.html')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                messages.warning(request,f'{username} registered Successfully')
                return redirect('student_login')
                # return render(request,'frontend/login.html')
        else:
            messages.warning(request,'PASSWORD MISMATCH')
            return render(request,'frontend/admin-signup.html') 
    else:    
        return render(request,'frontend/admin-signup.html')



def logout(request):
    messages.info(request,'You are logged our successfully')
    print('logout')
    auth.logout(request)
    return redirect('/')



def validate_candidate(request):
    if request.method=='POST':
        print("registration number is "+request.POST['reg_id'])
        reg_id=request.POST['reg_id']
        if institute_db.objects.filter(reg_id=reg_id).exists():
            if accepted_db.objects.filter(reg_id=reg_id).exists():
                registartion=accepted_db.objects.get(reg_id=reg_id).institute_id
                messages.info(request,f'Accepted : institute number is {registartion}')
                
            elif pending_db1.objects.filter(reg_id=reg_id).exists():
                messages.info(request,'Your Application is Still pending............')
            else:    
                messages.info(request,'Fill the Reporting form ')
                name=institute_db.objects.get(reg_id=reg_id).name
                return redirect('reporting-form')
        else:
            messages.info(request,'invalid registration id')
    return render(request,'frontend/reg_validate.html')


def reporting(request):
    print('this is reporting form')
    if request.method=='POST':
        reg_id=request.POST['reg_id']
        name=request.POST['name']
        dob=request.POST['dob']
        id_no=request.POST['id_no']
        address=request.POST['address']
        gender=request.POST['gender']
        file=request.FILES['file']
        image=request.FILES['image']
        course=request.POST['course']
        department=request.POST['department']
        specialization=request.POST['specialization']
        notes=request.POST['notes']

        document=pending_db1.objects.create(reg_id=reg_id,name=name,dob=dob,id_no=id_no,address=address,gender=gender,course=course,department=department,specialization=specialization,image=image,file=file,notes=notes)
        document.save()
        
        messages.info(request,f'{name} has Reported successfully ')
        return redirect('/')
    return render(request,'frontend/reporting-form.html')




def dynamic(request):
    return render(request,'frontend/dynamic.html')                



def dashboard(request):
    if request.method=='POST':
        print("id is "+request.POST['status'])
        if request.POST['status']!=str(0):
            print("id is "+request.POST['status'])
            datatoadd=pending_db1.objects.get(reg_id=request.POST['status'])
            savethis=accepted_db.objects.create(reg_id=datatoadd.reg_id,institute_id=datatoadd.reg_id,
                                                name=datatoadd.name,
                                                dob=datatoadd.dob,
                                                id_no=datatoadd.id_no,
                                                address=datatoadd.address,
                                                gender=datatoadd.gender,
                                                course=datatoadd.course,
                                                department=datatoadd.department,
                                                specialization=datatoadd.specialization,
                                                image=datatoadd.image,
                                                file=datatoadd.file,
                                                notes=datatoadd.notes
                                                )
            savethis.save()
            datatoadd.delete()
    
        
    pending_files=pending_db1.objects.all()
    
    print("call from dashboard")
    return render(request,'frontend/dashboard.html',{'pendings':pending_files})