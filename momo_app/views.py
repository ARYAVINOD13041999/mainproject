from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from momo_app.form import LoginRegister, customerform, workerform, complaintform, addform, scheduleform
from momo_app.models import customer, worker, complaint, add, schedule, appointment


# Create your views here.

def index(request):
    return render(request,'index.html')

def index1(request):
    return render(request,'index1.html')

def index2(request):
    return render(request,'index2.html')

def adminbase(request):
    return render(request,'admin/adminbase.html')


def customerbase(request):
    return render(request,'customer/customerbase.html')

def managerbase(request):
    return render(request,'manager/managerbase.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminbase')
            elif user.is_worker:
                return redirect('managerbase')
            elif user.is_customer:
                return redirect('customerbase')
        else:
                messages.info(request,'invalidcredentials')
    return render(request,'index1.html')



def customer_reg(request):
    form1 = LoginRegister()
    form2 = customerform()
    if request.method=='POST':
        form1=LoginRegister(request.POST)
        form2=customerform(request.POST)
        if form1.is_valid() and form2.is_valid():
            a=form1.save(commit=False)
            a.is_customer=True
            a.save()
            user1=form2.save(commit=False)
            user1.user=a
            user1.save()
            return redirect('login_view')
    return render(request,'customer/customer_reg.html',{'form1':form1,'form2':form2})


def registration(request):
    return render(request,'registration.html')



def worker_reg(request):
    form1 = LoginRegister()
    form2 = workerform()
    if request.method=='POST':
        form1=LoginRegister(request.POST)
        form2=workerform(request.POST)
        if form1.is_valid() and form2.is_valid():
            b=form1.save(commit=False)
            b.is_worker=True
            b.save()
            user1=form2.save(commit=False)
            user1.user=b
            user1.save()
            return redirect('login_view')
    return render(request,'manager/worker_reg.html',{'form1':form1,'form2':form2})

def customer_view(request):
    data = customer.objects.all()
    return render(request,'customer/customer_view.html',{'data':data})

def worker_view(request):
    data = worker.objects.all()
    return render(request,'manager/worker_view.html',{'data':data})


def delete(request,id):
    data = customer.objects.get(id=id)
    if request.method == 'POST':
          data.delete()
          return redirect('customer_view')

def update(request, id):
    data = customer.objects.get(id=id)
    form = customerform(instance=data)
    if request.method == 'POST':
        form = customerform(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('customer_reg')
    return render(request, 'update.html', {'form': form})

def delete1(request,id):
    data = worker.objects.get(id=id)
    if request.method == 'POST':
          data.delete()
          return redirect('worker_view')

def update1(request, id):
        data = worker.objects.get(id=id)
        form = customerform(instance=data)
        if request.method == 'POST':
            form = customerform(request.POST, instance=data)
            if form.is_valid():
                form.save()
                return redirect('worker_reg')
        return render(request, 'update1.html', {'form': form})

def feedback(request):
    form = complaintform()
    a = request.user
    if request.method == 'POST':
        form = complaintform(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = a
            data.save()
            return redirect('complaint')
    return render(request,'customer/complaint.html',{'form':form})


def complaint_adview(request):
    data= complaint.objects.all()
    return render(request,'complaint_adview.html',{'data':data})


def complaint_cusview(request):
    data = complaint.objects.all()
    return render(request,'complaint_cusview.html',{'data':data})


def replay(request,id):
    data= complaint.objects.get(id=id)
    if request.method == 'POST':
        r=request.POST.get('replay')
        data.replay=r
        data.save()
        messages.info(request,'Replay send for complaint')
        return redirect('soorya')
    return render(request, 'replay.html', {'data': data})


def notification(request):
    form = addform()
    if request.method == 'POST':
        form = addform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add')
    return render(request,'notification.html',{'form':form})

def notificationview(request):
    data = add.objects.all()
    return render(request,'notificationview.html',{'data':data})

def delete3(request,id):
    data = add.objects.get(id=id)
    if request.method == 'POST':
          data.delete()
          return redirect('view')

def seen(request):
    n = add.objects.all()
    return render(request,'seencustomer.html',{'n':n})

def seenworker(request):
    m = add.objects.all()
    return render(request,'seenworker.html',{'m':m})


def addschedule(request):
    form = scheduleform()
    if request.method == 'POST':
        form = scheduleform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('a')
    return render(request, 'schedule.html', {'form': form})

def view_schedule(request):
    data = schedule.objects.all()
    return render(request,'scheduleview.html',{'data':data})


def view_scheduleADMIN(request):
    data = schedule.objects.all()
    return render(request,'scheduleviewADMIN.html',{'data':data})


def delete_schedule(request,id):
    data = schedule.objects.get(id=id)
    if request.method == 'POST':
          data.delete()
          return redirect('c')


def take_appointment(request,id):
    a = schedule.objects.get(id=id)
    print(a)
    print('hello')
    u = customer.objects.get(user=request.user)
    print(u)
    print('hello')
    p = appointment.objects.filter(appointment=u,schedule=a)
    if p.exists():
        messages.info(request,'YOU HAVE ALREADY REQUESTED APPOINTMENT FOR THIS SCHEDULE')
        return redirect('b')
    else:
        if request.method == 'POST':
            obj = appointment()
            obj.appointment = u
            obj.schedule = a
            obj.save()
            messages.info(request,'appointment booked successfully')
            return redirect('soorya')
    return render(request,'take_appointment.html',{'a':a})

def view_appointment(request):
    data=appointment.objects.all()
    return render(request,'view_appointment.html',{'data':data})


def view_user_appointment(request):
    u = request.user
    cust = customer.objects.get(user=u)
    data= appointment.objects.filter(appointment=cust)
    return render (request,'customer/view_user_appointment.html',{'data':data})


def manager_view_appointment(request):
    data=appointment.objects.all()
    return render(request,'manager/manager_view_appointment.html',{'data':data})


def accept(request,id):
    data = appointment.objects.get(id=id)
    data.status=1
    data.save()
    messages.info(request,'Appointment confirmed')
    return redirect('manager_view_appointment')

def reject(request,id):
    data = appointment.objects.get(id=id)
    data.status=2
    data.save()
    messages.info(request,'Appointment rejected')
    return redirect('manager_view_appointment')


def customer_result(request):
    data=appointment.object.filter(appointment)










# def view_user_appointment(request):
#     return render(request,'view_user_appointment.html')






