from django.urls import path

from .views import QuotationCreateView, QuotationDetailView, ServerPing, QuotationDetailFromDBView, QuotationListView

app_name = 'quotation'

urlpatterns = [
    # sender api view
    path('', QuotationListView.as_view(), name='Quotation Entities List from Database'),
    path('database/<int:pk>', QuotationDetailFromDBView.as_view(), name='Quotation Entities from Database'),
    path('ping', ServerPing.as_view(), name='Server-Ping'),
    path('create', QuotationCreateView.as_view(), name='quotation-create'),
    path('<int:id>', QuotationDetailView.as_view(), name='quotation-detail'),
]
