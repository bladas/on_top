import json

from django.test import TestCase


# Create your tests here.
from utils.json_loader import load_file


class GoalTesting(TestCase):
    user_fixture = json.loads(load_file('fixtures/user_fixture.json'))

    def test1(self):
        self.assertEqual(self.user_fixture, 2)