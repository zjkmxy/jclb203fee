from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.template import RequestContext
from accounting.forms import TradeForm
from accounting.models import Trade, Category
from datetime import datetime
from operator import itemgetter, attrgetter

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

def ledger(request):
    """元帳ページ"""
    assert isinstance(request, HttpRequest)
    account_id = request.GET['account']
    account_title = Category.objects.filter(id=account_id)[0].name

    debit = Trade.objects.filter(dr_name__id=account_id)
    credit = Trade.objects.filter(cr_name__id=account_id)
    ret = [(cur.dating, cur.desc, True, cur.amount) for cur in debit]
    ret = ret + [(cur.dating, cur.desc, False, cur.amount) for cur in credit]
    ret = sorted(ret, key=itemgetter(0))
    return render(
        request,
        'general_ledger.html',
        {
            'account_title':account_title,
            'results':ret,
        }
    )