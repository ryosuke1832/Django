from django.shortcuts import render
from django.http import HttpResponse
from . forms import WellcmForm

def index(request):
    params = {
        'title' : 'Wellcome',
        'message' : '御登録受付フォーム：',
        'form' : WellcmForm
    }
    if (request.method == 'POST'):
        params['message'] = '名前:' + request.POST['name'] + '<br>メール:' + request.POST['mail'] + '<br>年齢:' + request.POST['age']
        params['form'] = WellcmForm(request.POST)
    return render(request, 'Wellcome/index.html', params)