from django.shortcuts import render
from django.http import HttpResponse
from .models import MemberList

def index(request):
    data = MemberList.objects.all()
    params = {
        'title': 'Wellcome',
        'message': 'all memberlist.',
        'data': data,
    }
    return render(request, 'Wellcome/index.html', params)