from django.test import TestCase
from app.calc import add

class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two number are added together"""
        self.assertEqual(add(5, 5), 10)
