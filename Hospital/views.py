from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
from .models import *
# Create your views here.

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()

    d = 0;
    p = 0;
    a = 0;

    for i in doctors:
        d+=1
    for i in patients:
        p+=1
    for i in appointments:
        a+=1
    d1 = {'d':d,'p':p,'a':a} 
    return render(request,'index.html',d1)

def Login(request):
    error=""
    if request.method=='POST':
       u = request.POST['uname']
       p = request.POST['pwd']

       user = authenticate(username =u,password=p)

       try:
           if user.is_staff:
               login(request,user)
               error ="no"
           else:
                error = "yes"

       except:
           error = "yes"
    d = {'error':error}
    return render(request,'login.html',d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def View_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html',d)

def Add_doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
       Fname = request.POST['First_name']
       Lname = request.POST['Last_name']
       contact = request.POST['contact']
       specilization = request.POST['specilization']

       try:
           Doctor.objects.create(First_name=Fname,Last_name=Lname,contact=contact,specilization=specilization)
           error ="no"
       except:
           error = "yes"
    d = {'error':error}
    return render(request,'add_doctor.html',d)

def Delete_Doctor(request,pid ):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Patient.objects.all()
    d = {'doc':doc}
    return render(request,'view_patient.html',d)

def Add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
       Fname = request.POST['First_name']
       Lname = request.POST['Last_name']
       Gender = request.POST['gender']
       Mobile = request.POST['mobile']
       address = request.POST['address']
       Symptoms = request.POST['Symptoms']

       try:
           Patient.objects.create(First_name=Fname,Last_name=Lname,gender=Gender,mobile=Mobile,address=address)
           error ="no"
       except:
           error = "yes"
    d = {'error':error}
    return render(request,'add_patient.html',d)


def Delete_Patient(request,pid ):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')


def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.all()
    d = {'appoint':appoint}
    return render(request,'view_appointment.html',d)

def Add_Appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method=='POST':
       doctor = request.POST['Doctor']
       patient = request.POST['Patient']
       date = request.POST['date']
       time = request.POST['time']
       doctor2 = Doctor.objects.filter(First_name=doctor).first()
       patient2 = Patient.objects.filter(First_name=patient).first()
       try:
           Appointment.objects.create(doctor=doctor2,patient=patient2,Date1=date,time1=time)
           error ="no"
       except:
           error = "yes"
    d = {'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'add_appointment.html',d)


def Delete_Appointment(request,pid ):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')