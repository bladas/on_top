import json

from django.test import TestCase
from accounts.tests import AccountTests
from utils.json_loader import load_file
from rest_framework.test import APIClient


class GoalTesting(TestCase):
    user_fixture = json.loads(load_file('fixtures/user_fixture.json'))
    api = APIClient()
    account_tests = AccountTests()

    def setUp(self) -> None:
        self.api.credentials()
        self.account_tests.test_register()
        user_resp = self.api.post('/authtoken/token/login', data=self.user_fixture, format='json')
        token = user_resp.data['auth_token']
        self.api.credentials(HTTP_AUTHORIZATION='Token ' + token)

    def test_create_goal(self):
        response = self.api.post('/dashboard/goals/', data={
            "title": "test1",
            "description": "test1"
        })
        self.assertEqual(response.status_code, 201)

    def test_get_goal_list(self):
        response = self.api.get('/dashboard/goals/')
        self.assertEqual(response.status_code, 200)
