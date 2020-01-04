from django.urls import path
from finances.views import TransactionMonthlyArchiveView
from finances import views

urlpatterns = [
    path('', views.home, name='finances-home'),
    path('add_budget_categories/', views.add_budget_categories,
         name='finances-add_budget_categories'),
    path('add_payment_methods/', views.add_payment_methods,
         name='finances-add_payment_methods'),
    path('save_payment_methods_form/', views.save_payment_methods_form,
         name='finances-save_payment_methods_form'),
    path('add_transactions/', views.add_transactions,
         name='finances-add_transactions'),
    path('save_transaction_form/', views.save_transaction_form,
         name='finances-save_transaction_form'),
    path('upload_transactions/', views.upload_transactions,
         name='finances-upload_transactions'),
    path('reports/<int:year>/<int:month>/', views.reports, name='finances-reports'),
    # Example: /2012/08/
    path(
        'historic_transactions/<int:year>/<int:month>/',
        TransactionMonthlyArchiveView.as_view(month_format='%m'),
        name='finances-archive_month_numeric'
    ),
]
