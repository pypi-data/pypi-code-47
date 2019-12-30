from rest_framework import generics

from .models import Sender
from .serializers import SenderSerializer


# Create your views here.


class SenderListView(generics.ListAPIView):
    """
    the api for listing all senders entity
    """
    queryset = Sender.objects.all()
    serializer_class = SenderSerializer


class SenderCreateView(generics.CreateAPIView):
    """
    the api for creating one specific sender entity
    """
    queryset = Sender.objects.all()
    serializer_class = SenderSerializer


class SenderDetailRetrieveView(generics.RetrieveAPIView):
    """
    the api for showing the sender entity detail
    """
    queryset = Sender.objects.all()
    serializer_class = SenderSerializer


class SenderDetailUpdateView(generics.UpdateAPIView):
    """
    the api for updateing the sender entity detail
    """
    queryset = Sender.objects.all()
    serializer_class = SenderSerializer

# class SenderListWithAttr():
