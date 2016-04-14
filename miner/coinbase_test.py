import unittest

from coinbase import serialize_coinbase_transaction


class CoinbaseTest(unittest.TestCase):
    def test_serialize_coinbase_transaction(self):
        # inspired from: http://bitcoin.stackexchange.com/a/20724
        # and https://en.bitcoin.it/wiki/Genesis_block
        reward = 5000000000
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
            "76a914" + pubkey_hash_hex + "88ac"
            "00000000"
        )
        serialized = serialize_coinbase_transaction(pubkey_hash, coinbase_data,
                                                    reward)

        self.assertEqual(expected, serialized)
