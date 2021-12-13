from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=128)
    age = models.IntegerField()

    class Meta:
        db_table = 'owners'

class dogs(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)

    class Meta:
        db_table = 'dongs'