from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.template import RequestContext
from accounting.forms import TradeForm
from accounting.models import Trade, Category
from datetime import datetime

# Create your views here.
def index(request):
    """ホームページ"""
    assert isinstance(request, HttpRequest)
    accounts = Category.objects.all()
    return render(
        request,
        'index.html',
        {
            'now_dt':datetime.now(),
            'accounts':accounts,
        }
    )

def addTrade(request):
    """取引記録追加"""
    if request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():
            new_trade = form.save()
            return HttpResponseRedirect('/test')

    form = TradeForm()
    return render(request, 'create_trade.html', {'form': form})

def journal(request):
    """仕訳帳ページ"""
    assert isinstance(request, HttpRequest)
    trades = Trade.objects.order_by('dating')
    return render(
        request,
        'journal.html',
        {
            'trades':trades,
        }
    )