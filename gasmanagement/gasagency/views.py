from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group


def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        gen=request.POST.get('gen')
        img=request.FILES.get('img')
        email=request.POST.get('email')
        paswd=request.POST.get('pswd')
        paswd2=request.POST.get('pswd2')

       

        if paswd!=paswd2:
            messages.error(request,"Password is diffrent")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already occurs")
            return redirect('register')
        
        user = User.objects.create_user(username=email, password=paswd, first_name=name )
        group = Group.objects.get(name="users")
        user.groups.add(group) 
        user.save()
        Register.objects.create(Name=name,dob=dob,Gen=gen,Img=img,Email=email,Pass=paswd,Cpass=paswd2,user=user)
        messages.success(request,"Registration Successfull!")
        return redirect('loginPage')
    return render(request,'userRegister.html')



def loginPage(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['paswd']
        user=authenticate(request,username=email,password=password) 
        if user is not None:
            login(request,user)
            
            if user.is_superuser:
                messages.success(request, "Login Successfully!")
                return redirect('admin_home')
            elif user.groups.filter(name="users").exists():
                messages.success(request,"Login Succcessfully!")
                return redirect('user')
            elif user.groups.filter(name="deliveragent").exists():
                messages.success(request,"Login Succcessfully!")
                return redirect('agentPanel')
            else:
                messages.error(request,"Invalid Users!")
            return render(request,'login.html')
            
        
        
        else:
            messages.error(request,"Invalid credencial!") 
    return render(request,'login.html')  


def user(request):
    return render(request,'User/userPanel.html')

def admin_home(request):
    return render(request,'Admin/adminPanel.html')

def zone(request):
    if request.method=='POST':
        zone=request.POST['zone']
        z=Zone.objects.create(zone=zone)
        z.save()
        messages.success(request,"Zone added successfully!")
        return redirect('viewZone')
    return render(request,'Admin/manageZone.html')

def editzone(request,id):
    edit=Zone.objects.get(id=id)
    if request.method=="POST":
        edit.zone=request.POST['zone']
        edit.save()
        return redirect('viewZone')
    return render(request,'Admin/EditZone.html',{'edit':edit})

def viewZone(request):
    Z=Zone.objects.all()
    return render(request,'Admin/viewZone.html',{'Zones':Z})

def deleteZone(request,id):
    edit=Zone.objects.get(id=id)
    edit.delete()
    return redirect('viewZone')

# def booking(request):
#     if request.method=="POST":
#         type=request.POST['type']
#         weight=request.POST['weight']
#         price=request.POST['price']
#         qty=request.POST['qty']

#         cylinder=Cylinder.objects.create(Type=type,Weight=weight,Price=price,Quantity=qty)
#         cylinder.save()
#         messages.success(request,"Booking Confirmed!")
#         return redirect('user')
#     return render(request,'User/BookCylinder.html')

def bookingView(request):
    user = Register.objects.get(user=request.user)
    cylinder = Booking.objects.filter(user=user)
    return render(request,'User/bookingView.html',{'cylin':cylinder})

def feedback(request):
    if request.method=="POST":
        date=request.POST['date']
        customer=Register.objects.get(user=request.user)
        message=request.POST['message']
        rating=request.POST['rating']
        Feedback.objects.create(Date=date,customer=customer,Message=message,Rating=rating)
    return render(request,'User/Feedback.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def addAgent(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        licence=request.POST['licence']
        phone=request.POST['phone']
        email=request.POST['email']
        location=request.POST['location']
        date=request.POST['date']
        import random
        password=random.randint(0000,9999)
        print(password)
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('addAgent')
        user = User.objects.create_user(
            username=email,
            password=str(password),
            first_name=name
        )
        print("Email :", email)
        print("Password :", password)
        group = Group.objects.get(name="deliveragent")
        user.groups.add(group)
        user.save()
        Agents.objects.create(Name=name,Age=age,Licence=licence,Phone=phone,Email=email,Location=location,Joining=date,user=user)
        return redirect('manageAgent')
    return render(request,'Admin/addAgent.html')

def manageAgent(request):
    view=Agents.objects.all()
    return render(request,'Admin/manageAgent.html',{'views':view})

def editAgent(request,gas_id):
    view=Agents.objects.get(id=gas_id)

    if request.method=="POST":
        view.Name=request.POST['name']
        view.Age=request.POST['age']
        view.Licence=request.POST['licence']
        view.Phone=request.POST['phone']
        view.Email=request.POST['email']
        view.Location=request.POST['location']
        view.Joining=request.POST['date']
        view.save()
        return redirect('manageAgent')
    return render(request,'Admin/EditAgent.html',{'views':view})

def deleteAgent(request,gas_id):
    view=Agents.objects.get(id=gas_id)
    view.delete()
    return redirect('manageAgent')

def viewBooking(request):

    Book=Booking.objects.filter(status='pending')
    return render(request,'Admin/viewBooking.html',{'book':Book})

def viewFeedback(request):
    Data=Feedback.objects.all()
    return render(request,'Admin/viewFeedback.html',{'data':Data})

def agentPanel(request):
    agent=Agents.objects.get(user=request.user)
    return render(request,'Agent/agentPanel.html',{'agent':agent})


def assignAgent(request,booking_id):
    booking=Booking.objects.get(id=booking_id)
    agent=Agents.objects.all()

    if request.method=="POST":
         agent_id=request.POST['agent']
         p=AssignAgent(booking_id=booking_id,agent_id=agent_id)
         p.save()
        
         

         return redirect('admin_home')

    return render(request, 'Admin/assignAgent.html', {
        'booking': booking,
        'agents': agent
    })

def viewAssigned(request):
    
    agent = Agents.objects.get(user=request.user)
    bookings = AssignAgent.objects.filter(agent=agent,status='Pending')
    return render(request, 'Agent/viewAssigned.html', {
        'bookings': bookings})


def agent_accept(request,id):
    o=AssignAgent.objects.get(id=id)
    o.status='accepted'
    o.save()
    booking=o.booking
    booking.status='accepted'
    booking.save()
    return redirect('/agentPanel/')


def agent_reject(request,id):
    o=AssignAgent.objects.get(id=id)
    o.status='pending'
    o.save()
    return redirect('/agentPanel/')

def acceptedOrder(request):
    agent=Agents.objects.get(user=request.user)
    order=AssignAgent.objects.filter(agent=agent,status='accepted')
    return render(request,'Agent/acceptedOrders.html',{'order':order})



def manageCylinder(request):
    if request.method=="POST":
        type=request.POST['type']
        price=request.POST['price']
        net=request.POST['net']
        avail=request.POST['avail']
       
        Cylinder.objects.create(Type=type,Price=price,Net=net,Available=avail)
    return render(request,'Admin/manageCylinder.html')

def viewCylinder(request):
    cylinder=Cylinder.objects.all()
    return render(request,'Admin/viewCylinder.html',{'cylinder':cylinder})

def editcylinder(request,id):
    cylinder=Cylinder.objects.get(id=id)
    if request.method=="POST":
        cylinder.Type=request.POST['type']
        cylinder.Price=request.POST['price']
        cylinder.Available=request.POST['avail']
        cylinder.Net=request.POST['net']
        cylinder.save()
        return redirect('admin_home')
    return render(request,'Admin/editcylinder.html',{'cylinder':cylinder})

def deletecylinder(request,id):
    cylinder=Cylinder.objects.get(id=id)
    cylinder.delete()
    return redirect('viewCylinder')


def booking(request):
    res=Cylinder.objects.all()
    return render(request,'User/BookCylinder.html',{'cylinder':res})

def bookingLink(request,id):
    cylinder = Cylinder.objects.get(id=id)
    customer = Register.objects.get(user=request.user)
    from datetime import date
    today = date.today()
    already_booked = Booking.objects.filter(
        user=customer,bookingdate__year=today.year,
        bookingdate__month=today.month
        
    ).exists()
    if already_booked:
        messages.error(request,"Already Booked This Month!")
        return redirect('booking')
    obj = Booking()
    obj.cylinder = cylinder
    obj.user = customer
    obj.price = cylinder.Price
    obj.status = "Pending"
    obj.save()
    messages.success(request, "Cylinder booked successfully!")

    if cylinder.Available<=0:
        messages.error(request,"Cylinder out of stock")
        return redirect('boookingView')
    cylinder.Available-=1
    cylinder.save()
    return render(request,'User/bookingLink.html')
def complete_get(request):
     o=request.user
     p=Agents.objects.get(user_id=o.id)
     t=AssignAgent.objects.filter(agent_id=p.id,status="completed")
     print("pppppppppp",t)

     
     return render(request,'Agent/completed.html',{'booking':t})


def complete_post(request,id):
    p=Booking.objects.get(id=id)
    p.status="completed"
    p.save()
    o=AssignAgent.objects.get(booking_id=id)
    o.status="completed"
    o.save()
    return redirect('/agentPanel/')

    

def feedbackView(request):
    cust=Register.objects.get(user=request.user)
    feedback=Feedback.objects.filter(customer=cust)  
    return render(request,'User/feedbackView.html',{'feedback':feedback})
  












    


    








        



