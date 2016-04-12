import unittest

from coinbase import calculate_block_reward, serialize_coinbase_transaction


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

    def test_serialize_coinbase_transaction(self):
        # inspired from: http://bitcoin.stackexchange.com/a/20724
        # and https://en.bitcoin.it/wiki/Genesis_block
        height = 0
        txs = []

        coinbase_data_hex = "0100"
        coinbase_data = bytes.fromhex(coinbase_data_hex)
        pubkey_hash_hex = "5399c3093d31e4b0af4be1215d59b857b861ad5d"
        pubkey_hash = bytes.fromhex(pubkey_hash_hex)
        expected = bytes.fromhex(
            "01000000"
            "01"
            "0000000000000000000000000000000000000000000000000000000000000000"
            "ffffffff" +
            "0" + str(len(coinbase_data)) +
            coinbase_data_hex +
            "ffffffff"
            "01"
            "00F2052A01000000"
            "19"
            "76a814" + pubkey_hash_hex + "88ac"
            "00000000"
        )
        serialized = serialize_coinbase_transaction(pubkey_hash, coinbase_data,
                                                    height, txs)

        self.assertEqual(expected, serialized)
