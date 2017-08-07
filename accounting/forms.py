from django.forms import ModelForm
from accounting.models import Trade

class TradeForm(ModelForm):
    class Meta:
        model = Trade
        fields = ['dating', 'desc', 'dr_name', 'cr_name', 'amount', 'label', ]