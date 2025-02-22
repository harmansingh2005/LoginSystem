
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    if request.method == "POST":
        # Get form data
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        password2 = request.POST.get("pass2")

        # Check if passwords match
        if password != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("signup")

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("signup")

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect("signup")

        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = fname
        user.last_name = lname
        user.is_staff = False
        user.save()

        messages.success(request, "Your account has been created! You can now log in.")
        return redirect("mylogin")
    return render(request,"authentication/signup.html")

def mylogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password) # Checking if the user exists in database
        if user is not None: # If the user exists
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect("home")
        else: 
            messages.error(request, "Invalid username or password!")
            return redirect("mylogin")     
    return render(request,"authentication/login.html") 

def logout(request):
    return render(request,"authentication/logout.html")