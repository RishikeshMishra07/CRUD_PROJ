

from django.db import models

class students(models.Model):
    
    stuid = models.CharField(max_length=100, default='1')
    stuname = models.CharField(max_length=200)
    stuemail = models.EmailField(max_length=254)
    stuage = models.IntegerField()


