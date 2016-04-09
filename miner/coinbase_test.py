import unittest

from coinbase import calculate_block_reward


class CoinbaseTest(unittest.TestCase):
    class TransactionMock:
        def __init__(self):
            self.fees = 100000

    def test_block_reward_genesis_no_fees(self):
        height = 0
        txs = []

        value = calculate_block_reward(height, txs)

        self.assertEqual(5000000000, value)

    def test_block_reward_genesis_fees(self):
        height = 0
        txs = [CoinbaseTest.TransactionMock()]

        value = calculate_block_reward(height, txs)

        self.assertEqual(5000100000, value)

    def test_block_reward_no_halving_no_fees(self):
        height = 209999
        txs = []

        value = calculate_block_reward(height, txs)

        self.assertEqual(5000000000, value)

    def test_block_reward_no_halving_fees(self):
        height = 209999
        txs = [CoinbaseTest.TransactionMock()]

        value = calculate_block_reward(height, txs)

        self.assertEqual(5000100000, value)

    def test_block_reward_first_halving_no_fees(self):
        height = 210000
        txs = []

        value = calculate_block_reward(height, txs)

        self.assertEqual(2500000000, value)

    def test_block_reward_first_halving_fees(self):
        height = 210000
        txs = [CoinbaseTest.TransactionMock()]

        value = calculate_block_reward(height, txs)

        self.assertEqual(2500100000, value)

    def test_block_reward_max_halving_no_fees(self):
        height = 2**64
        txs = []

        value = calculate_block_reward(height, txs)

        self.assertEqual(0, value)
