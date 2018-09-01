from django.shortcuts import render
from formUser.forms import usrForm as u1
from formUser.models import User

def usrForm(request):
    form = u1()

    if request.method == 'POST':

        form = u1(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'user.html' , {'form':form})

def index(request):
    data = User.objects.all()
    return render(request,'usr/index.html',{'data':data})