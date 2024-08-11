from os import name
from django.contrib import messages
from django.db.models.expressions import Value
from django.forms.widgets import ChoiceWidget
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import semFour,semThree,semOne,semTwo,notificationsLive
from django.core.files.storage import FileSystemStorage
from .forms import semfourControl, semoneControl, semthreeControl, semtwoControl
# Create your views here.

def home(request):
    notifications = notificationsLive.objects.all()
    return render(request, 'base.html',{'notification':notifications})

def login_view(request):
     if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('logged')
        else:
            messages.info(request, "*Invalid Username/Password")
        
     return render(request, 'login.html')


def register_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]

        if User.objects.filter(username=username).exists():
            messages.info(request, '*Username is already taken')
            return redirect('register')
        else:
            newuser = User.objects.create_user(username=username,password=password,email=email,first_name=fname,last_name=lname)
            newuser.save()
            messages.info(request, 'Registerd Successfully please login to Continue')
            return redirect('login')
    return render(request, 'register.html')

@login_required(login_url='/login/')
def logged_view(request):
    return redirect('semone')

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def semone_view(request):
    if request.method == "POST":
        selected_option = request.POST["optionname"]
        notes = semOne.objects.filter(select_sub=selected_option)
    else:
        notes = semOne.objects.all()
    return render(request, 'semnotes/sem1.html',{'notes':notes})

@login_required(login_url='/login/')
def semtwo_view(request):
    if request.method == "POST":
        selected_option = request.POST["optionname"]
        notes = semTwo.objects.filter(select_sub=selected_option)
    else:
        notes = semTwo.objects.all()
    return render(request, 'semnotes/sem2.html',{'notes':notes})
        

@login_required(login_url='/login/')
def semthree_view(request):
    if request.method == "POST":
        selected_option = request.POST["optionname"]
        notes = semThree.objects.filter(select_sub=selected_option)
    else:
        notes = semThree.objects.all()
    return render(request, 'semnotes/sem3.html',{'notes':notes})

@login_required(login_url='/login/')
def semfour_view(request):
    if request.method == "POST":
        selected_option = request.POST["optionname"]
        notes = semFour.objects.filter(select_sub=selected_option)
    else:
        notes = semFour.objects.all()
    return render(request, 'semnotes/sem4.html',{'notes':notes})

@login_required(login_url='/login/')
def admin_view(request):
    form1 = semoneControl(request.POST, request.FILES)
    form2 = semtwoControl(request.POST, request.FILES)
    form3 = semthreeControl(request.POST, request.FILES)
    form4 = semfourControl(request.POST, request.FILES)

    context = {}
    
    optionsem = None
    
    if request.method == "POST":
        optionsem = request.POST.get('semoption')
        context['sem'] = optionsem
    if optionsem == "one":
        context['form'] = form1
    elif optionsem == "two":
        context['form'] = form2
    elif optionsem == "three":
        context['form'] = form3
    elif optionsem == "four":
        context['form'] = form4
    else:
        context['form'] = form1        
    

    if request.method == "POST":
        if context is not None:
            if context['form'].is_valid():
                context['form'].save()
                return redirect(('/'))
        else:
            messages.info(request,'Fields Cannot be empty')
        
    return render(request, 'admin/admin.html',context)

@login_required(login_url='/login/')
def profile_view(request):
    context = {}
    context['present_user'] = request.user

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        newuser = User.objects.update(first_name=first_name,last_name=last_name)
        return redirect('profile')
        
    return render(request,'profile.html',context)

@login_required(login_url='/login/')
def delete_profile(request):
    user = request.user
    d_user = User.objects.filter(username=user.username)
    d_user.delete()
    return redirect('login')
    