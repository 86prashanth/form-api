from django.shortcuts import render
from .mangal import StudentRegistration
# Create your views here.f
def home(request):
    form=StudentRegistration()
    return render(request,'app/home.html',{'form':form})
    