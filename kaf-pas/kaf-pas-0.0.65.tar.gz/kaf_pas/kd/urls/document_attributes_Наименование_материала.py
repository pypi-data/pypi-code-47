from django.urls import path

from kaf_pas.kd.views import document_attributes_Наименование_материала

urlpatterns = [

    path('Document_attributes_Наименование_материала/Fetch/', document_attributes_Наименование_материала.Document_attributes_Наименование_материала_Fetch),
    path('Document_attributes_Наименование_материала/Add', document_attributes_Наименование_материала.Document_attributes_Наименование_материала_Add),
    path('Document_attributes_Наименование_материала/Update', document_attributes_Наименование_материала.Document_attributes_Наименование_материала_Update),
    path('Document_attributes_Наименование_материала/Remove', document_attributes_Наименование_материала.Document_attributes_Наименование_материала_Remove),
    path('Document_attributes_Наименование_материала/Lookup/', document_attributes_Наименование_материала.Document_attributes_Наименование_материала_Lookup),
    path('Document_attributes_Наименование_материала/Info/', document_attributes_Наименование_материала.Document_attributes_Наименование_материала_Info),
    path('Document_attributes_Наименование_материала/Copy', document_attributes_Наименование_материала.Document_attributes_Наименование_материала_Copy),

]
