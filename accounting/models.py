from django.db import models
from accounting.utils import formatDate
from django.db.models import Sum

# Create your models here.
class Label(models.Model):
    """
    類別
    """
    name = models.CharField(u'Name', max_length=10)

    def __str__(self):
        return self.name

class Category(models.Model):
    """
    勘定科目
    """
    name = models.CharField(u'Name', max_length=20)

    def __str__(self):
        return self.name

    def balance(self):
        """残高計算"""
        # 借方
        debit  = Trade.objects.filter(dr_name=self).aggregate(Sum('amount'))['amount__sum']
        if debit is None:
            debit = 0
        # 貸方
        credit = Trade.objects.filter(cr_name=self).aggregate(Sum('amount'))['amount__sum']
        if credit is None:
            credit = 0
        # 残高
        return debit - credit

class Trade(models.Model):
    """
    取引
    """
    # 日付
    dating = models.DateField(u'Dating')
    # 摘要
    desc = models.CharField(u'Desc', max_length=200)
    # 借方科目
    dr_name = models.ForeignKey('Category', related_name='Debit')
    # 貸方科目
    cr_name = models.ForeignKey('Category', related_name='Credit')
    # 金額（借方＝貸方）
    amount = models.IntegerField(u'Amount')
    # 類別区分
    label = models.ForeignKey('Label')

    def __str__(self):
        return '{} {} {}->{} {}円'.format(formatDate(self.dating), self.desc, self.cr_name, self.dr_name, self.amount)