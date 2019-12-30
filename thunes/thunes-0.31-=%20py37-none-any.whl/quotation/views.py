import json
import random

import requests
from django.shortcuts import get_object_or_404
from django.core import serializers
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from thunes.APIAccessGrant import APIAccessGrant

from .models import Quotation, Source, Destination
from .serializers import QuotationSerializer

# Create your views here.


class QuotationDetailView(APIView):
    """
    the api for showing the quotation entity detail by ID by external API
    """

    def get(self, request, id, format=None):
        APIObject = APIAccessGrant('/quotations/' + str(id))
        apiprams = APIObject.parmReturn()

        response = requests.get(apiprams['urlparm'], headers={
            'X-TransferTo-apikey': apiprams['apikey'],
            'X-TransferTo-nonce': apiprams['nonce'],
            'X-TransferTo-hmac': apiprams['hmac'],
            'Date': apiprams['date'],
            # 'Content-Type': 'application/json',
        })
        return Response(response.json())


class QuotationCreateView(APIView):
    """
    the api for creating the quotation entity
    """
    quotation_body = {
        "external_id": "148118432398",
        "payer_id": "1669",
        "mode": "SOURCE_AMOUNT",
        "source": {
            "amount": 10,
            "country_iso_code": "SGP",
            "currency": "SGD"
        },
        "destination": {
            "amount": None,
            "currency": "GHS"
        }
    }

    def post(self, request, *args, **kwargs):
        # import random to generate different external id
        self.quotation_body['external_id'] = str(148118432398 + random.randint(0, 10000000000))
        APIObject = APIAccessGrant('/quotations/')
        apiprams = APIObject.parmReturn()

        # the method to get the key
        (response_body, value), = request.data.items()

        self.quotation_body['source'] = json.loads(response_body)['source']
        self.quotation_body['destination'] = json.loads(response_body)['destination']

        response = requests.post(apiprams['urlparm'], headers={
            'X-TransferTo-apikey': apiprams['apikey'],
            'X-TransferTo-nonce': apiprams['nonce'],
            'X-TransferTo-hmac': apiprams['hmac'],
            'Date': apiprams['date'],
            'Content-Type': 'application/json',
        }, json=self.quotation_body)
        if response.json().get('errors', None) is None:
            # Enable this function to store the quotation data
            self.createquotationentity(self.quotation_body, response.json()['id'])
        return Response(response.json())

    def createquotationentity(self, data, quotation_id):
        """
        the function to create the quotation entity
        """
        try:
            quotationentity = Quotation.objects.get(external_id=data['external_id'], quotation_id=quotation_id)
        except Quotation.DoesNotExist:
            sourceentity = Source.objects.create(
                country_iso_code=data['source']['country_iso_code'],
                currency=data['source']['currency'],
                amount=data['source']['amount']
            )
            destinationentity = Destination.objects.create(
                currency=data['destination']['currency'],
                amount=data['destination']['amount']
            )
            quotationentity = Quotation.objects.create(
                quotation_id=quotation_id,
                external_id=data['external_id'],
                payer_id=data['payer_id'],
                mode=data['mode'],
                source=sourceentity,
                destination=destinationentity
            )


class QuotationListView(generics.ListAPIView):
    """
    the function to get the quotation entities list from database
    """
    serializer_class = QuotationSerializer
    quotation_List = []
    quotaion_entity = {}

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        # Clean the quotation list memory
        self.quotation_List.clear()

        quotationqueryset = Quotation.objects.all()
        serializer = self.get_serializer(quotationqueryset, many=True)
        for quotation in serializer.data:
            self.quotaion_entity.clear()
            sourceEntity = Source.objects.filter(id=quotation['source']).values()
            destinationEntity = Destination.objects.filter(id=quotation['destination']).values()
            self.quotaion_entity['quotaion_id'] = quotation['quotation_id']
            self.quotaion_entity['external_id'] = quotation['external_id']
            self.quotaion_entity['mode'] = quotation['mode']
            self.quotaion_entity['source'] = list(sourceEntity)[0]
            self.quotaion_entity['destination'] = list(destinationEntity)[0]
            self.quotation_List.append(self.quotaion_entity)
        return Response(self.quotation_List)


class QuotationDetailFromDBView(generics.RetrieveAPIView):
    """
    the function to get the quotation entity from database
    """
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer
    quotaion_entity = {}

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.quotaion_entity.clear()
        instance = self.get_object()
        print(instance.source.id)
        sourceEntity = Source.objects.filter(id=instance.source.id).values()
        destinationEntity = Destination.objects.filter(id=instance.destination.id).values()
        self.quotaion_entity['quotaion_id'] = instance.quotation_id
        self.quotaion_entity['external_id'] = instance.external_id
        self.quotaion_entity['mode'] = instance.mode
        self.quotaion_entity['source'] = list(sourceEntity)[0]
        self.quotaion_entity['destination'] = list(destinationEntity)[0]
        return Response(self.quotaion_entity)


class ServerPing(APIView):

    def get(self, request, format=None):
        """
        the function to test the backend API's connectivity
        """
        APIObject = APIAccessGrant('')
        apiprams = APIObject.parmReturn()

        pingUrl = apiprams['urlparm'].replace('v1/money-transfer', 'ping')

        # Enable this function to store the quotation data
        # self.createquotationentity(request.data)

        response = requests.get(pingUrl, headers={
            'X-TransferTo-apikey': apiprams['apikey'],
            'X-TransferTo-nonce': apiprams['nonce'],
            'X-TransferTo-hmac': apiprams['hmac'],
            'Date': apiprams['date'],
        })
        return Response(response.json())

