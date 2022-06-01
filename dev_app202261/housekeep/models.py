from django.db import models
from regist_login.models import User

# Create your models here.
class Session(models.Model):
    session_num = models.IntegerField('セッション番号')
    name = models.CharField('あだ名', max_length=255)
    def __str__(self):
        return self.name

class Billing(models.Model):
    user_name = models.CharField('あだ名', max_length=255)
    created_date = models.DateField('作成日')
    cost = models.IntegerField('値段',default=0)
    category = models.CharField('タグ',max_length=255)
    detail = models.CharField('商品名',max_length=255)

    def __str__(self):
        return self.detail + '：' + str(self.cost)