from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from myapp1.forms import LoginForm, RegisterForm
from myapp1.models import Worker, Adopters


def index_page(request):
    # I get data from html-form using POST method and comparing with name atrribute of form
    if request.method == 'POST':
        name = request.POST['first-name']
        last_name = request.POST['last-name']
        email_address = request.POST['email']
        phone_number = request.POST['phone']
        pet = request.POST['pet']
        info_additional = request.POST['bio']
        new_adopter = Adopters(name=name, second_name=last_name, email_address=email_address, phone_number=phone_number,
                               pet_adopt=pet, info_additional=info_additional)
        new_adopter.save()

    # return request = html site
    return render(request, 'index.html')


def welcome_page(request):
    return render(request, 'welcome.html')


def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('welcome')

        form = LoginForm()
        return render(request, 'login_page.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"Hi {username.title()}, welcome back!")
                return redirect('welcome')

        messages.error(request, f'Invalid username or password')
        return render(request, 'login_page.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, f"You have been logged out.")
    return redirect('login')


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have signed up succesfully.')
            login(request, user)
            return redirect('welcome')
        else:
            return render(request, 'register.html', {'form': form})




def about_page(request):
    # I get all objects from database
    all_workers = Worker.objects.all()

    # I use data dictionary which I can use in html django
    return render(request, 'about.html', {'data': all_workers})

# Create your views here.
