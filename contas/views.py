from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Transacao

# Create your views here.
def home(request):
    data ={}
    # data['transacoes'] = ['t1','t2','t3']
    # data['now'] = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, 'contas/home.html', data)


def listagem(request):
    data= {}
    return render(request, 'contas/listagem.html', data)