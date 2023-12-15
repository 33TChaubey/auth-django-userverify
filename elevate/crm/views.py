from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginFrom
#Authentication models and function
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def homepage(request):
    
    return render(request, 'crm/index.html')


def register(request):
    
    form  = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm:my-login')
        
    context = {
        'registerform': form
    }
    
    
    return render(request, 'crm/register.html', context)

def my_login(request):
    
    form  = LoginFrom()
    if request.method == 'POST':
        form = LoginFrom(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('crm:dashboard')
    context = {
        'loginform':form
    }
    return render(request, 'crm/my-login.html', context)

def logout_view(request):
    
    auth.logout(request)
    
    return redirect ("")

def dashboard(request):
    
    return render(request, 'crm/dashboard.html')