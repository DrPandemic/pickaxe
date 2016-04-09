import unittest

from coinbase import calculate_coinbase_value


class CoinbaseTest(unittest.TestCase):
    def test_coinbase_value_genesis_no_fees(self):
        height = 0
        fees = 0

        value = calculate_coinbase_value(height, fees)

        self.assertEqual(5000000000, value)

    def test_coinbase_value_genesis_fees(self):
        height = 0
        fees = 100000

        value = calculate_coinbase_value(height, fees)

        self.assertEqual(5000100000, value)

    def test_coinbase_value_no_halving_no_fees(self):
        height = 209999
        fees = 0

        value = calculate_coinbase_value(height, fees)

        self.assertEqual(5000000000, value)

    def test_coinbase_value_no_halving_fees(self):
        height = 209999
        fees = 100000

        value = calculate_coinbase_value(height, fees)

        self.assertEqual(5000100000, value)

    def test_coinbase_value_first_halving_no_fees(self):
        height = 210000
        fees = 0

        value = calculate_coinbase_value(height, fees)

        self.assertEqual(2500000000, value)

    def test_coinbase_value_first_halving_fees(self):
        height = 210000
        fees = 100000

        value = calculate_coinbase_value(height, fees)

        self.assertEqual(2500100000, value)

    def test_coinbase_value_max_halving_no_fees(self):
        height = 2**64
        fees = 0

        value = calculate_coinbase_value(height, fees)

        self.assertEqual(0, value)
