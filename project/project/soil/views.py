# from soil.models import User_Login
from .models import Crops, Fertilisers
from email import message
from django.contrib import messages
from turtle import title
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.

def index(request):
    return render(request, 'soil/home.html')

def fertiliser_solution(request):
    return render(request, 'soil/fertiliser_solution.html', {'title':'Fertiliser Solutions'})


def crop(request):
    predicted_crops = Crops.objects.all()
    if request.method == 'POST':
        Nitrogen = request.POST.get('Nitrogen')
        print(Nitrogen)
        Phosphorous = request.POST.get('Phosphorous')
        Potassium = request.POST.get('Potassium')
        Temperature = request.POST.get('Temperature')
        Humidity = request.POST.get('Humidity')
        pH_Level = request.POST.get('pH_Level')
        Rainfall = request.POST.get('Rainfall')
        for a in predicted_crops:
            if (int(a.Nitrogen) == int(Nitrogen)):
                print(Nitrogen)
                print(a.Crop_Name)

    return render(request, 'soil/crop.html', {'title': 'Crop'})

def fertiliser(request):
    fertilisers = Fertilisers.objects.all()
    if request.method == 'POST':
        Nitrogen = request.POST.get('Nitrogen')
        Phosphorous = request.POST.get('Phosphorous')
        Potassium = request.POST.get('Potassium')
        pH_Level = request.POST.get('pH_Level')
        Soil_Moisture = request.POST.get('Soil_Moisture')
        Crop_Name = request.POST.get('Crop_Name')
        for a in fertilisers:
            if ((str(a.Crop_Name)).capitalize() == str(Crop_Name)):
                if (int(a.Nitrogen) < int(Nitrogen)):
                    messages.info(request, 'Adding composted manure to the soil. Planting a green manure crop, such as borage. Planting nitrogen-fixing plants like peas or beans. Adding coffee grounds to the soil.')
                if (int(a.Phosphorous) < int(Phosphorous)):
                    messages.info(request, 'Composted manure neutralizes the soil, which increased phosphorus availability. Bone meal releases in soil have a whopping 15% phosphorus concentration. Rock phosphate provides a steady rate of phosphorus over many years. Fish meal boosts the nutrients of plants containing phosphorus.')
                if (int(a.Potassium) < int(Potassium)):
                    messages.info(request, 'Add banana peels as they are very high in potassium. Wood ash can also be used to increase the potassium deficiency in soil. Greensand will also add potassium to your garden.')
                if (int(a.pH_Level) < int(pH_Level)):
                    messages.info(request, "Use organic materials (such as pine needles, compost, or composted manure, can lower your soil's pH). Consider applying sulfur. Adding aluminum sulfate.")
                if (int(a.pH_Level) > int(pH_Level)):
                    messages.info(request, 'If the soil is too acidic add a base like Liming material (pulverized, hydrated, granules, and pellets) to increase the pH of the Soil. Water the soil regularly. Use Wood Ashes (The ash of burned trees will add calcium, potassium, and boron).')
        return render(request, 'soil/fertiliser_solution.html', {'title':'Fertiliser Solutions'})
    else:
        return render(request, 'soil/fertiliser.html', {'title': 'Fertiliser'})



def user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:

            messages.info(request, 'Invalid Credentials!')
            return render(request, 'soil/user-login.html', {'title': 'User Login'})
    return render(request, 'soil/user-login.html', {'title': 'User Login'})
    

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    # first_name = request.POST.get('first_name')
    # print(first_name)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('Username not available')
                messages.info(request, 'Username not available')
                return render(request, 'soil/register.html', {'title': 'Register'})
            elif User.objects.filter(email=email).exists():
                print('Email ID already exists')
                messages.info(request, 'Email ID already exists')
                return render(request, 'soil/register.html', {'title': 'Register'})
            else:
                user = User.objects.create_user(first_name = first_name, last_name = last_name, email = email, username = username, password = password1)
                user.save()
                print('User Created Successfully')
                return render(request,'soil/user-login.html', {'title': 'User Login'})
        else:
            print('Password not matching')
            messages.info(request, 'Password not matching')
            return render(request, 'soil/register.html', {'title': 'Register'})
    else:
        return render(request, 'soil/register.html', {'title': 'Register'})
