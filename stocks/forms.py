from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['date', 'trade_code', 'high', 'low', 'open', 'close', 'volume']

    success_url = '/your/success/url/' 