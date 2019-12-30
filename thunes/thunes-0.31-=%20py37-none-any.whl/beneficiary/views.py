from rest_framework import generics

from .models import Beneficiary
from .serializers import BeneficiarySerializer

# Create your views here.


class BeneficiaryListView(generics.ListAPIView):
    """
    the api for listing all beneficiaries entity
    """
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer


class BeneficiaryCreateView(generics.CreateAPIView):
    """
    the api for creating one specific beneficiary entity
    """
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer


class BeneficiaryDetailRetrieveView(generics.RetrieveAPIView):
    """
    the api for showing the one specific beneficiary entity by ID
    """
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer


class BeneficiaryDetailUpdateView(generics.UpdateAPIView):
    """
    the api for updateing the beneficiary entity detail by ID
    """
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer
