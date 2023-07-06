from django.shortcuts import render
from app.Forms import *
from django.http import HttpResponse

def djform(request):
    sfo=signup()
    d={'sfo':sfo}
    if request.method=='POST':
        sfd=signup(request.POST)
        if sfd.is_valid():
            n=sfd.cleaned_data['name']
            return HttpResponse(n)
    return render(request,'djform.html',d)
