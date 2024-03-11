from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import SignupForm,UserLoginForm


def signup(request):
    if request.method == 'POST':  # Correct method check
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'maineapp/register.html', {'form': form})


def homepage(request):
    return render(request,'maineapp/Mainpage.html')

def user_login(request):
    if request.method=='POST':
        form = UserLoginForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user= authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form = UserLoginForm
    return render(request,'maineapp/login.html',{'form':form})
