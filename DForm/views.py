from django.shortcuts import render
from django.http import HttpResponse
from DForm.forms import *
from DForm.models import *
# Create your views here.

def sf(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            print(str(SFD.cleaned_data))
            Student.objects.get_or_create(name=SFD.cleaned_data['name'],age=SFD.cleaned_data['age'],cls=SFD.cleaned_data['cls'],loc=SFD.cleaned_data['loc'],email=SFD.cleaned_data['email'])[0].save()
            return HttpResponse('Data recieved successfully ')
        else:
            return HttpResponse('Invalid data entered')
    return render(request,'sf.html',d)

'''
def django_forms(request):
    SUO=SignUp()
    d={'SUO':SUO}
    if request.method=='POST':
        DSO=SignUp(request.POST)
        if DSO.is_valid():
            DSignUp.objects.get_or_create(name=DSO.cleaned_data['name'],age=DSO.cleaned_data['age'],course=DSO.cleaned_data['course'],email=DSO.cleaned_data['email'],password=DSO.cleaned_data['password'],gender=DSO.cleaned_data['gender'],address=DSO.cleaned_data['address'])[0].save()
            return HttpResponse('Data gathering finished successfully')
    return render(request,'django_forms.html',d)
'''