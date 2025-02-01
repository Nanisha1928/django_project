from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not all([username, name, email, password]):
            messages.error(request, 'All fields are required.')
            return render(request, 'register.html')

        try:
            with connection.cursor() as cursor:
                q = "INSERT INTO registerdetails (username, name,  email, password) VALUES ('{}','{}','{}','{}')".format(username, name, email, password)
                cursor.execute(q)
                messages.success(request, "Registration successful.Please log in.")
                return redirect('log_in')

        except Exception as e:
            messages.error(request, f"Error:{str(e)}")
            return render(request, 'register.html')

    return render(request, 'register.html')

def log_in(request):
    with connection.cursor() as cursor:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            query = "INSERT INTO logindetails (username, password) VALUES ('{}','{}')".format(username, password)
            cursor.execute(query)

            if not all([username, password]):
                messages.error(request, "Both fields are required.")
                return render(request, 'log_in.html')

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return render(request,'carbon.html')
            else:
                messages.error(request, "Invalid credentials. Please try again.")
                return render(request, 'log_in.html')

        return render(request, 'log_in.html')

def log_out(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('log_in')

def carbon(request):
    electricity = travel = meat = total = 0
    if request.method == "POST":
        try:
            # Get values from the form
            electricity = int(request.POST.get("electricity", 0))
            travel = int(request.POST.get("travel", 0))
            meat = int(request.POST.get("meat", 0))

            # Carbon footprint calculation logic
            # Example: Electricity = 0.5 kg CO₂ per kWh, Travel = 0.2 kg CO₂ per km, Meat = 2 kg CO₂ per kg
            total = (electricity * 0.5) + (travel * 0.2) + (meat * 2)
        except ValueError:
            total = "Invalid input. Please enter numeric values only."

    # Render the template with calculated values
    return render(request, 'carbon.html', {
        'electricity': electricity,
        'travel': travel,
        'meat': meat,
        'total': total,
        })