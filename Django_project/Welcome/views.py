from django.shortcuts import render
from django.http import HttpResponse
from Welcome.forms import WelcmForm

def index(request):
    params ={
        'title':'Wellcome',
        'message':'ご登録受付フォーム',
        'form':WelcmForm

    }
    if (request.method == 'POST'):
        params['message'] = '名前' + request.POST['name'] + '<br>メール:' + request.POST['mail'] + '<br>年齢' +request.POST['age']
        params['form'] = WelcmForm(request.POST)
    return render(request, 'Welcome/index.html',params)
