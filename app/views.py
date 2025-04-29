from django.shortcuts import redirect, render
from app.models import *
from django.contrib.auth.models import User,AnonymousUser
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q

def index(request):

    reviews = Review.objects.all()
    return render(request,'index.html',{'reviews' : reviews})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = Contact(name=name,email=email,subject=subject,message=message)
        data.save()

    return render(request,'contact.html')

def signupUser(request):

    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')   

        if(pass1 != pass2):
            return redirect('signup')

        Myuser = User.objects.create_user(username, email, pass1)
        Myuser.save()

        return redirect('login')
    
    return render(request,'signup.html')

def loginUser(request):
    
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request,'login.html')
        
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        trip = request.POST.get('trip_select')
        star = request.POST.get('star_select')   
        message = request.POST.get('message')

        Myreview = Review(name=name,city=city,trip=trip,star=star,message=message)
        Myreview.save()

    return render(request,'review.html')

def profile(request):
    return render(request,'profile.html')

def package(request):

    context = Package.objects.all()

    if 'search' in request.GET:
        search_term = request.GET['search']
        context = Package.objects.all().filter(Q(name__icontains=search_term) | Q(city__icontains=search_term))
    
    return render(request,'package.html',{'context':context})