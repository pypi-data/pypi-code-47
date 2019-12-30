from django.urls import path
from .views import SenderListView, SenderCreateView, SenderDetailRetrieveView, SenderDetailUpdateView

app_name = 'sender'

urlpatterns = [
    # sender api view
    path('', SenderListView.as_view(), name='senders-list'),
    path('', SenderCreateView.as_view(), name='senders-create'),
    path('<int:pk>', SenderDetailRetrieveView.as_view(), name='sender-entity-by-id-retrieve'),
    path('<int:pk>', SenderDetailUpdateView.as_view(), name='sender-entity-by-id-update'),
    # path('attr', SenderDetailUpdateView.as_view(), name='sender-list-attribute'),
]