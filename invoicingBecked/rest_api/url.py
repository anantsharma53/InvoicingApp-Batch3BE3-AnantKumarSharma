from django.urls import path
from .import views
from .views import InvoiceView,ItemEntryViews,GetInvoiceViews,GetSingleInvoiceViews,SigneUpView,SigneInView
# GetInvoiceViews,ItemEntryViews
from django.views.decorators.csrf import csrf_exempt
urlpatterns =[ 
    path('invoices/', GetInvoiceViews.as_view(), name='invoice-list'),
    path('invoices/new/',csrf_exempt(InvoiceView.as_view()),name='new-invoice-create'),
    path('invoices/<int:id>/',GetSingleInvoiceViews.as_view(),name='invoice-single-list'),
    path('invoices/<int:id>/items',csrf_exempt(ItemEntryViews.as_view()),name='new-invoice-create'),
    path('invoices/user/signup/',csrf_exempt(SigneUpView.as_view()),name='user-signup'),
    path('invoices/user/login/',csrf_exempt(SigneInView.as_view()),name='user-login'),
]