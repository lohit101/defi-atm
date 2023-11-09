from django.db import models

# Create your models here.
class Server1(models.Model):
    name = models.CharField(verbose_name="Name", max_length=20, null=False, blank=False)
    card = models.IntegerField(verbose_name="Card Number", max_length=16, null=False)
    pin = models.IntegerField(verbose_name="Card PIN", max_length=4, null=False)
    balance = models.IntegerField(verbose_name="Balance", max_length=100, null=False, default=0)

    def __str__(self):
        return self.name

class Server2(models.Model):
    name = models.CharField(verbose_name="Name", max_length=20, null=False, blank=False)
    card = models.IntegerField(verbose_name="Card Number", max_length=16, null=False)
    pin = models.IntegerField(verbose_name="Card PIN", max_length=4, null=False)
    balance = models.IntegerField(verbose_name="Balance", max_length=100, null=False, default=0)

    def __str__(self):
        return self.name
        