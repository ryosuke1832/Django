from django.shortcuts import render
from django.http import HttpResponseBadRequest
from Welcome.models import MemberList

def index(request):
    data = MemberList.objects.all()
    params = {
        'title':'Welcome',
        'message':'all memberlist',
        'data':data,
    }
    return render(request,'Welcome/index.html',params)
