from django.db import models

# Create your models here.
class User(models.Model):
    e_mail = models.EmailField('メールアドレス')
    password = models.CharField('パスワード',max_length=255)
    name = models.CharField('name',max_length=255)

    def __str__(self):
        return self.name + ' ' + self.e_mail