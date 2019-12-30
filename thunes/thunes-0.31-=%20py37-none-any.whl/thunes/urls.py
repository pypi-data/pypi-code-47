"""thunes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

adminpatterns = [
    path('admin/', admin.site.urls),
]

documentspatterns = [
    path('api/docs/', include_docs_urls(title='Thunes Test Apis')),
]

urlpatterns = adminpatterns + documentspatterns + [
    path('api/v1/', include([
        path('senders/', include('sender.urls', namespace='sender_api')),
        path('beneficiaries/', include('beneficiary.urls', namespace='beneficiary_api')),
        path('transactions/', include('transaction.urls', namespace='transaction_api')),
        path('quotation/', include('quotation.urls', namespace='quotation_api')),
    ])),
]
