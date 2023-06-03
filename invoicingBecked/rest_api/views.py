from django.shortcuts import render
from django.views import View
from .serializers import InvoiceSerializer,itemSerializer,UserSerializer
from django.http import HttpResponse,JsonResponse,HttpResponseBadRequest,Http404
import json
# Create your views here.
invoices = [{
        "invoice_id": 1,
        "client_name": "Anant Sharma",
        "date": "2023-05-30",
        "items": [
            {
                "desc": "product 1",
                "rate": 100.00,
                "quantity": 2,
            }
        ],
    }]
user=[{
    "user_id":1,
    "email":"abc@gmail.com",
    "password":"abc123",
}]


class InvoiceView(View):
    def post(self, request):
        invoice_data=json.loads(request.body)
        invoice_data['invoice_id'] = len(invoices)+1
        print(invoice_data)
        invoice_serialized=InvoiceSerializer(data=invoice_data)
        print(invoice_serialized)
        print(invoice_serialized.is_valid())
        if(invoice_serialized.is_valid()):
            invoices.append(invoice_serialized.data)
            return JsonResponse(invoice_serialized.data, status=200)
        else:
            return HttpResponseBadRequest()

class GetInvoiceViews(View):
    def get(self, request):
        invoice_serialized=InvoiceSerializer(invoices,many=True).data
        return JsonResponse(invoice_serialized,safe=False)

class GetSingleInvoiceViews(View):
    def get(self,request,id):
        invoice_data=[{}]
        for val in invoices:
            if val["invoice_id"]==id:
                invoice_serialized=InvoiceSerializer(val).data
                return JsonResponse(invoice_serialized, safe=False)
        else:
            raise Http404("invoice not found")
    
class ItemEntryViews(View):
    def post(self, request,id):
        item_data=json.loads(request.body)
        item_serialized=itemSerializer(data=item_data)
        if(item_serialized.is_valid()):
            #Find the review to update
            for val in invoices:
                if val["invoice_id"]==id:
                    val["items"].append(item_data)
            return JsonResponse({"message":"items added succesfully"}, status=200)
        return HttpResponseBadRequest()
    
    

class SigneUpView(View):
    def post(self,request):
        user_data=json.loads(request.body)
        user_data["user_id"]=len(user)+1
        user_serialized=UserSerializer(data=user_data)
        if(user_serialized.is_valid() and user_serialized):
            user.append(user_serialized.data)
            print(user)
            return JsonResponse(user_serialized.data,status=200) 
        else:
            return HttpResponseBadRequest(status=401)


class SigneInView(View):
    def post(self,request):
        user_data=json.loads(request.body)
        print(user_data)
        for val in user:
            if(val["email"]==user_data["email"] and val["password"]==user_data["password"]):
                # token=generate_token(user_data)
                print(val)
                break
            return JsonResponse({'token': user_data["email"]},safe=False,status=200)
        return HttpResponseBadRequest("Error") 























# class GetInvoiceViews(View):
#     def get(self, request):
#         # invoice_serialized=InvoiceSerializer(invoices).data
#         return JsonResponse(invoices,safe=False)
# [
                #     {
                #     'desc': val["items.desc"],
                #     'rate': val["items"].rate,
                #     'quantity': val["items"].quantity,
                #     }
                #     # for item in val.items.all()
                # ],