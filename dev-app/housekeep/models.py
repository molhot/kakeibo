from django.db import models
from regist_login.models import User

# Create your models here.
class Session(models.Model):
    session_num = models.IntegerField('セッション番号')
    name = models.CharField('あだ名', max_length=255)
    def __str__(self):
        return self.name