
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')  
        
        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different one.")
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use. Please choose a different one.")
            return redirect('register')

        # Create new user if no existing username or email
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Assign the role to the user (optional, based on your app's requirements)
        if role == 'admin':
            user.groups.add(Group.objects.get(name='admin'))
        elif role == 'staff':
            user.groups.add(Group.objects.get(name='staff'))
        elif role == 'guest':
            user.groups.add(Group.objects.get(name='guest'))
        
        user.save()
        

        messages.success(request, "Registration successful! Please log in.")
        
        return redirect('login')

    return render(request, 'register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role') 

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if role == 'admin' and user.groups.filter(name='admin').exists():
                auth_login(request, user)
                return redirect('home')
            elif role == 'staff' and user.groups.filter(name='staff').exists():
                auth_login(request, user)
                return redirect('home')
            elif role == 'guest' and user.groups.filter(name='guest').exists():
                auth_login(request, user)
                return redirect('home')
            else:
                # Role mismatch, show error message
                messages.error(request, "Invalid role or role mismatch.")
                return redirect('login')
        else:
            # Authentication failed, show error message
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')
