from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from .models import Student
from django.contrib import messages
from django.http import HttpResponse

def say_hello(request):
    return render(request,'students/hello.html',{ 'name':'ross'})

def home(request):
    students = Student.objects.all()
    return render(request,'students/homepage.html',{"students":students})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('upass')
        
        user = authenticate(request,username = username,password = password)
        user = authenticate(request, username=username, password=password)

        print("AUTH RESULT:", user)

        if user is not None:
            login(request, user)  # login success
            return redirect('home')  # redirect to home page
        else:
            messages.error(request, "Invalid username or password")
   
    return render(request,'students/login.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('rname')
        password = request.POST.get('rpass')
        cpass = request.POST.get('cpass')
        email = request.POST.get('eml')

        if(cpass == password):
            User.objects.create_user(
                username = username,
                email = email,
                password = password
                    
            )
        else:
            messages.warning(request,'Password mistmatch!!!')
            return redirect('signup')


    messages.success(request,'Account created')
    return render(request, 'students/signup.html')

def add_view(request):
    if request.method == 'POST':
        name = request.POST.get('sname')
        course = request.POST.get('course')
        gpa = request.POST.get('gpa')
        sid = request.POST.get('sid')

        s1 = Student(sname = name , course = course, gpa = gpa, sid= sid)
        s1.save()
        Student.objects.all()
    return render(request,"students/add.html")

def edit(request,id):
    student = Student.objects.get(id = id)
    if request.method == 'POST':
        student.sname = request.POST.get('name')
        student.sid = request.POST.get('sid')
        student.course = request.POST.get('course')
        student.gpa = request.POST.get('gpa')
        student.save()
        return redirect('home')
    return render(request,"students/edit.html",{"student":student })

def delete(request,id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('home')

def search(request):
    query = request.GET.get('search-name', '').strip()

    if query:
        students = Student.objects.filter(sname__icontains=query)
    else:
        students = Student.objects.none()   # empty queryset

    return render(
        request,
        'students/search.html',
        {'students': students, 'query': query}
    )
