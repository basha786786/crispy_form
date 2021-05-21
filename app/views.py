from django.shortcuts import render

# Create your views here.
from app.forms import *
def Contact(request):
    form=ContactForm()
    return render(request,'crispy.html',context={'form':form})
