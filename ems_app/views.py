from django.shortcuts import render, HttpResponse, redirect
from ems_app.models import Employee, Department  # Import models
from ems_app.forms import EmployeeForm  # Import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    employee = Employee.objects.all()
    department = Department.objects.all()
    return render(request, 'index.html', {"employee": employee, 'department': department})

def about(request):
    return render(request, 'about.html')
@login_required
def add_data(request):
    eForm = EmployeeForm()
    if request.method == "POST":
        eForm = EmployeeForm(request.POST)
        if eForm.is_valid():
            eForm.save()
            print("Data saved successfully")
            return redirect('home')  # Redirect to the home view
    return render(request, "add_data.html", {'form': eForm})

def register(request):
    form=UserCreationForm()
    if(request.method=='POST'):
        form=UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('home')

    return render(request,"user_registeration.html",{"form":form})
def login_view(request):
    if(request.method=='POST'):
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"login successful")
            return redirect('home')
        else:
            messages.error(request,"Invaild user Name or Password")
    return render(request,"login.html")
def logout_view(request):
    logout(request)
    return redirect("login")  

def contact_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        age = request.POST.get('age')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')

        # Tum yahan pe data ko validate ya process kar sakte ho
        # Jaise print karna ya kisi external API ko bhejna
        print("Username:", username)
        print("Age:", age)
        print("Email:", email)
        print("Feedback:", feedback)

        messages.success(request, 'Form submitted successfully!')
        return render(request, 'contact.html')  # Redirect karna optional hai

    return render(request, 'contact.html')
def update_data(request,id):
    employee=Employee.objects.get(id=id)
    if(request.method == 'POST'):
        eForm  = EmployeeForm(request.POST, instance=employee)
        if(eForm.is_valid()):
            eForm.save()
            print("Data update successfully")  
            return redirect('home')
    else:
        eForm = EmployeeForm(instance=employee)
    return render(request, "add_data.html", {'form':eForm , 'employee':employee}) 

def delete_data(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('home')