from logging import PlaceHolder
from django import forms
from .models import Billing

class SpendingBilling(forms.Form):
    choices = (
        ('食費', '食費'),
        ('水道費', '水道費'),
        ('光費', '光費'),
        ('ガス代', 'ガス代'),
        ('学習費', '学習費'),
        ('娯楽費', '娯楽費'),
        ('ムダ費', 'ムダ費'),
        ('家賃','家賃')
    )
    #choicesの左がデータベース登録名、右が選択肢名

    created_date = forms.DateTimeField(label='日付')
    cost = forms.IntegerField(label='費用')
    category = forms.ChoiceField(choices = choices, label='カテゴリー')
    detail = forms.CharField(
        max_length=255,
        label='用途',
    )