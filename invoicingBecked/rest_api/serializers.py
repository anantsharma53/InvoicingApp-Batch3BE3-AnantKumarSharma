from rest_framework import serializers
from .models import Invoice,item,User
class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model=item
        # fields='__all__'
        fields = ['desc', 'quantity', 'rate']

class InvoiceSerializer(serializers.ModelSerializer):
    items = itemSerializer(many=True)
    class Meta:
        model = Invoice
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"