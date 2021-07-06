from unittest import TestCase

from app.logic import operations


class TestLogicTestCase(TestCase):
    def test_plus(self):
        result = operations(4, 5, '+')
        self.assertEqual(9, result)

    def test_minus(self):
        result = operations(4, 5, '-')
        self.assertEqual(-1, result)

    def test_multiple(self):
        result = operations(4, 5, '*')
        self.assertEqual(20, result)
