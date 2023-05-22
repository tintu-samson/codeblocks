from django.shortcuts import render,redirect
from .models import Domain,Events
from .forms import createUserForm
from .decorators import unauthenticated_user
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    domain = Domain.objects.all()
    events = Events.objects.all()
    context = {'domain':domain,'events':events}
    return render(request,"myapp/index.html",context)

@unauthenticated_user
def signup(request): 
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request,"myapp/signup.html",context)

@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            messages.info(request,"Username or Password is incorrect")
            return redirect('login')
    
    return render(request,"myapp/login.html")

def logout_user(request):
    logout(request)
    return redirect('/')