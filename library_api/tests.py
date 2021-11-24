from django.test import TestCase
from rest_framework.test import APIClient

# Create your tests here.
class TestSum(TestCase):
        def test_returns_the_sum_of_two_numbers(self):
                client = APIClient()

                client.get('/api/sum',{'n1':5, 'n2':10})

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.data['result'], 15)

class TestRest(TestCase):
        def test_returns_the_rest_of_two_numbers(self):
                client = APIClient()

                client.get('/api/rest',{'n1':10, 'n2':5})

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.data['result'], 5)