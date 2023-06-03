from django.db import models

# Create your models here.

class Invoice(models.Model):
    invoice_id=models.IntegerField()
    client_name=models.CharField(max_length=200)
    date=models.CharField(max_length=11)

class item(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items',null=True, blank=True)
    desc=models.CharField(max_length=200)
    quantity=models.IntegerField()
    rate=models.DecimalField(max_digits=10, decimal_places=2)

class User (models.Model):
    user_id=models.IntegerField()
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=16)