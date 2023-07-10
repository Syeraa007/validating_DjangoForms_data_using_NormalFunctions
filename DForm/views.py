from django.shortcuts import render
from django.http import HttpResponse
from DForm.forms import *
# Create your views here.

def sf(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
        else:
            return HttpResponse('Invalid data entered')
    return render(request,'sf.html',d)