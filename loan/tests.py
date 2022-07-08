from rest_framework import status
from rest_framework.test import APITestCase

from loan.models.solicitation import Solicitation
from loan.serializers.solicitation_serializer import SolicitationSerializer

from loan.models.installment import Installment
from loan.models.client import Client
from loan.serializers.client_serializer import ClientSerializer
from loan.models.bank import Bank

class TestCaseSetUp():
  def execute(self):
    Installment.objects.create(
      number=1, interest=20.5, value=300, full_value=361.5, comission=100)
    Bank.objects.create(
      label="003 - Banco da Amazonia S.A.", account_type_label="CC", account_number=12345)
    Client.objects.create(
      name="Cliente", phone=21999999999, cpf=12345678911, bank=Bank.objects.get(pk=1))
    Solicitation.objects.create(
      client=Client.objects.get(pk=1), installment=Installment.objects.get(pk=1), card_number=55562132144, desired_value=2500, total_loan=3000
    )
class SolicitationTestCase(APITestCase):
  
  def setUp(self):
    TestCaseSetUp.execute(self)
  
  def test_solicitation_post(self):
    data = {
        "client": 1,
        "installment": 1,
        "card_number": 38123456789,
        "desired_value": 1500,
        "total_loan": 2000
    }
    response = self.client.post("/solicitations/", data, format="json")
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
  def test_empty_client_solicitation_post(self):
    data = {
      "client": '',
      "installment": 1,
      "card_number": 21123456789,
      "desired_value": 7000,
      "total_loan": 8000
    }
    response = self.client.post("/solicitations/", data, format="json")
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
  def test_empty_desired_value_solicitation_post(self):
    data = {
      "client": 1,
      "installment": 1,
      "card_number": 21123456789,
      "desired_value": '',
      "total_loan": ''
    }
    response = self.client.post("/solicitations/", data, format="json")
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
  def test_empty_installment_solicitation_post(self):
    data = {
      "client": 1,
      "installment": '',
      "card_number": 21123456789,
      "desired_value": 1500,
      "total_loan": 2000
    }
    
    response = self.client.post("/solicitations/", data, format="json")
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
  def test_solicitation_get_all(self):
    response = self.client.get("/solicitations/")
    solicitations = Solicitation.objects.all()
    serialized_solicitations = SolicitationSerializer(solicitations, many=True)
    self.assertEqual(response.data, serialized_solicitations.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

class ClientTestCase(APITestCase):
  def setUp(self):
    TestCaseSetUp.execute(self)

  def test_get_single_valid_client(self):
    response = self.client.get("/clients/", {"cpf": 12345678911})
    client = Client.objects.get(cpf=12345678911)
    serialized_client = ClientSerializer(client)
    print(response.data)
    print(serialized_client.data)
    self.assertEqual(response.json(), serialized_client.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)