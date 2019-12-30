import requests
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from thunes.APIAccessGrant import APIAccessGrant


from django.db.models import Q

from django.shortcuts import get_object_or_404

from .models import Transaction, CreditPartyIdentity
from .serializers import TransactionSerializer

from sender.models import Sender
from beneficiary.models import Beneficiary
from quotation.models import Quotation, Source, Destination
# Create your views here.


class TransactionListView(generics.ListAPIView):
    """
    the api for listing all transactions entities
    """
    serializer_class = TransactionSerializer
    transaction_list = []
    transaction_entity = {}
    quotation_entity = {}

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        self.transaction_list.clear()

        status = self.request.GET.get('status', None)
        if status == 'CREATED':
            status_class = '1'
            queryset = Transaction.objects.filter(status_class=status_class).values()
        elif status == 'CONFIRMED':
            status_class = '2'
            queryset = Transaction.objects.filter(status_class=status_class).values()
        else:
            queryset = Transaction.objects.filter().values()
        transactionlist = list(queryset)
        for transaction in transactionlist:
            quotationentity = Quotation.objects.filter(id=transaction['quotation_id']).values()
            transaction['quotation_id'] = list(quotationentity)
            sourceentity = Source.objects.filter(id=quotationentity[0]['source_id']).values()
            destinationentiy = Destination.objects.filter(id=quotationentity[0]['destination_id']).values()
            quotationentity[0]['source_id'] = list(sourceentity)[0]
            quotationentity[0]['destination_id'] = list(destinationentiy)[0]
            transaction['quotation_id'] = list(quotationentity)[0]
            self.transaction_list.append(transaction)
        return Response(self.transaction_list)


class TransactionCreateView(APIView):
    """
    the api for creating an transaction entity based on the quotation entity
    """

    def post(self, request, quotation_id, *args, **kwargs):
        APIObject = APIAccessGrant('/quotations/' + str(quotation_id) + '/transactions')
        apiprams = APIObject.parmReturn()

        response = requests.post(apiprams['urlparm'], headers={
            'X-TransferTo-apikey': apiprams['apikey'],
            'X-TransferTo-nonce': apiprams['nonce'],
            'X-TransferTo-hmac': apiprams['hmac'],
            'Date': apiprams['date'],
            'Content-Type': 'application/json',
        }, json=request.data)
        if response.json().get('errors', None) is None:
            self.transactioncreate(request.data, response.json()['id'], quotation_id)
        return Response(response.json())

    def transactioncreate(self, data, transaction_id, quotation_id):
        """
        the function for creating the transaction entity
        """
        try:
            quotationentity = Quotation.objects.get(quotation_id=quotation_id)
            transactionentity = Transaction.objects.get(external_id=data['external_id'], quotation=quotationentity)
        except Transaction.DoesNotExist:
            senderentity = self.sendercreate(data['sender'])
            beneficiaryentity = self.beneficiarycreate(data['beneficiary'])
            self.creditpartyidentity(data['credit_party_identifier'])
            transactionentity = Transaction.objects.create(
                transaction_id=transaction_id,
                quotation=quotationentity,
                sender=senderentity,
                beneficiary=beneficiaryentity,
                external_id=data['external_id'],
                retail_fee_currency=data['retail_fee_currency'],
                purpose_of_remittance=data['purpose_of_remittance'],
                # retail_fee=data['retail_fee']
            )

    def sendercreate(self, senderdata):
        """
        the function for creating the sender entity
        """
        try:
            senderentity = Sender.objects.get(lastname=senderdata['lastname'], firstname=senderdata['firstname'])
            return senderentity
        except Sender.DoesNotExist:
            senderentity = Sender.objects.create(
                lastname=senderdata['lastname'],
                firstname=senderdata['firstname'],
                nationality_country_iso_code=senderdata['nationality_country_iso_code'],
                date_of_birth=senderdata['date_of_birth'],
                country_of_birth_iso_code=senderdata['country_of_birth_iso_code'],
                gender=senderdata['gender'],
                address=senderdata['address'],
                postal_code=senderdata['postal_code'],
                city=senderdata['city'],
                country_iso_code=senderdata['country_iso_code'],
                msisdn=senderdata['msisdn'],
                email=senderdata['email'],
                id_type=senderdata['id_type'],
                id_number=senderdata['id_number'],
                id_delivery_date=senderdata['id_delivery_date'],
                occupation=senderdata['occupation']
            )
        return senderentity

    def beneficiarycreate(self, beneficiarydata):
        """
        the function for creating the beneficiary entity
        """
        try:
            beneficiaryentity = Beneficiary.objects.get(lastname=beneficiarydata['lastname'],
                                                        firstname=beneficiarydata['firstname'])
            return beneficiaryentity
        except Beneficiary.DoesNotExist:
            beneficiaryentity = Beneficiary.objects.create(
                lastname=beneficiarydata['lastname'],
                firstname=beneficiarydata['firstname'],
                nationality_country_iso_code=beneficiarydata['nationality_country_iso_code'],
                date_of_birth=beneficiarydata['date_of_birth'],
                country_of_birth_iso_code=beneficiarydata['country_of_birth_iso_code'],
                gender=beneficiarydata['gender'],
                address=beneficiarydata['address'],
                postal_code=beneficiarydata['postal_code'],
                city=beneficiarydata['city'],
                country_iso_code=beneficiarydata['country_iso_code'],
                msisdn=beneficiarydata['msisdn'],
                email=beneficiarydata['email'],
                id_type=beneficiarydata['id_type'],
                id_number=beneficiarydata['id_number'],
                occupation=beneficiarydata['occupation']
            )
        return beneficiaryentity

    def creditpartyidentity(self, creditdata):
        """
         the function for creating the credit party identity entity
        """
        try:
            creditentity = CreditPartyIdentity.objects.get(
                msisdn=creditdata['msisdn'],
                bank_account_number=creditdata['bank_account_number'],
                swift_bic_code=creditdata['swift_bic_code']
            )
        except CreditPartyIdentity.DoesNotExist:
            creditentity = CreditPartyIdentity.objects.create(
                msisdn=creditdata['msisdn'],
                bank_account_number=creditdata['bank_account_number'],
                swift_bic_code=creditdata['swift_bic_code']
            )


class TransactionConfirmView(APIView):
    """
    the api for confirming the transaction has been created.
    """

    def post(self, request, transactionDB_id, *args, **kwargs):
        transactionEntity = get_object_or_404(Transaction, id=transactionDB_id)
        APIObject = APIAccessGrant('/transactions/' + transactionEntity.transaction_id + '/confirm')
        apiprams = APIObject.parmReturn()

        response = requests.post(apiprams['urlparm'], headers={
            'X-TransferTo-apikey': apiprams['apikey'],
            'X-TransferTo-nonce': apiprams['nonce'],
            'X-TransferTo-hmac': apiprams['hmac'],
            'Date': apiprams['date'],
            'Content-Type': 'application/json',
        }, json=request.data)
        if response.json().get('errors', None) is None:
            self.transactionconfirm(transactionDB_id)
        return Response(response.json())

    def transactionconfirm(self, transaction_id):
        """
        the function to confirm the transaction entity in database
        """
        try:
            transactionentity = Transaction.objects.get(id=transaction_id)
            transactionentity.status = '20000'
            transactionentity.status_message = '20000'
            transactionentity.status_class = '2'
            transactionentity.status_class_message = '2'
            transactionentity.save()
        except Transaction.DoesNotExist:
            pass


class TransactionDetailRetrieveView(generics.RetrieveAPIView):
    """
    the api for showing the transactoin entity detail
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetailUpdateView(generics.UpdateAPIView):
    """
    the api for updating the transaction entity detail
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class BeneficiaryListBySenderName(generics.RetrieveAPIView):
    """
    the api for showing Beneficiary based on the given sender name
    """
    beneficiary_list = {}
    beneficiary_list_result = []

    def get(self, request, *args, **kwargs):
        lastname = self.request.GET.get('lastname', None)
        firstname = self.request.GET.get('firstname', None)
        # Add the clear function to not create too much memory space for these two para
        self.beneficiary_list.clear()
        self.beneficiary_list_result.clear()

        if lastname is None and firstname is None:
            pass
        elif lastname is None or firstname is None:
            pass
        else:
            senderentity = self.getsenderentity(lastname, firstname)
            beneficiaryentities = Transaction.objects.filter(Q(sender=senderentity)).values('beneficiary_id')
            # for loop to get a beneficiary map with beneficiary_id as key and
            # occurancy of this beneficiary as the value
            for beneficiary in beneficiaryentities:
                if beneficiary['beneficiary_id'] in self.beneficiary_list.keys():
                    self.beneficiary_list[beneficiary['beneficiary_id']] += 1
                else:
                    self.beneficiary_list[beneficiary['beneficiary_id']] = 1
            sorted(self.beneficiary_list.values())
            for key in self.beneficiary_list.keys():
                beneficiary_single_entity = self.getbeneficiary(key)
                self.beneficiary_list_result.append({'beneficiary_id': key,
                                                'beneficiary_name': beneficiary_single_entity.__str__(),
                                                'counter': self.beneficiary_list[key]})
        return Response(self.beneficiary_list_result)

    def getsenderentity(self, lastname, firstname):
        """
        the function for get the sender entity by its lastname and firstname
        """
        if firstname is not None and lastname is not None:
            try:
                return Sender.objects.get(firstname=firstname, lastname=lastname)
            except Sender.DoesNotExist:
                return None
        elif firstname is not None:
            try:
                return Sender.objects.get(firstname=firstname)
            except Sender.DoesNotExist:
                return None
        else:
            try:
                return Sender.objects.get(lastname=lastname)
            except Sender.DoesNotExist:
                return None
        return None

    def getbeneficiary(self, pk):
        try:
            return Beneficiary.objects.get(pk=pk)
        except Beneficiary.DoesNotExist:
            return None

