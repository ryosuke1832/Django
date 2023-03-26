from django.db import models

class MemberList(models.Model):
    name = models.CharField('名前', max_length=100)
    mail = models.EmailField('メール', max_length=100)
    gender = models.BooleanField('性別')
    age = models.IntegerField('年齢', default=0)
    address = models.CharField('住所', max_length=100)
    
    def __str__(self):
        return'<MemberList:id=' + str(self.id) + ',' + self.name + '(' + str(self.age) + ')>'