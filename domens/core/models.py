from django.db import models

class Webserver(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name='Название')
    class Meta:
        verbose_name =  'Веб сервер'
        verbose_name_plural = 'Веб серверы'

    def __str__(self):
        return self.name
        
class Domens(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name='Название')
    webserver = models.CharField(max_length=7, choices=(('nginx','nginx'),('apache2','apache2')), verbose_name='Сервер')
    status = models.BooleanField(default=False,verbose_name='Cтатус')

    class Meta:
        verbose_name =  'Домен'
        verbose_name_plural = 'Домены'

    def __str__(self):
        return self.name
        
