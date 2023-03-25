from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    welcm_data = {
        'day':'2023年3月23日木曜日',
        'weather':'晴れ',

    }
    return render(request,
                  'Welcome/index.html',
                  welcm_data,)


