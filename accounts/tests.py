import json

from django.test import TestCase

from utils.json_loader import load_file
from rest_framework.test import APIClient


class AccountTests(TestCase):
    user_fixture = json.loads(load_file('fixtures/user_fixture.json'))
    api = APIClient()

    def test_register(self):
        response = self.api.post('/auth/users/', data=self.user_fixture, format='json')
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        self.test_register()
        response = self.api.post('/authtoken/token/login', data=self.user_fixture, format='json')
        self.assertEqual(response.status_code, 200)
