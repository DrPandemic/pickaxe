import unittest

from transaction import Transaction


class TransactionTest(unittest.TestCase):
    def test_ctor_hashes_data(self):
        # taken from:
        # http://bitcoin.stackexchange.com/q/2859
        data = bytes.fromhex(
            "01000000010000000000000000000000"
            "00000000000000000000000000000000"
            "0000000000ffffffff4d04ffff001d01"
            "04455468652054696d65732030332f4a"
            "616e2f32303039204368616e63656c6c"
            "6f72206f6e206272696e6b206f662073"
            "65636f6e64206261696c6f757420666f"
            "722062616e6b73ffffffff0100f2052a"
            "01000000434104678afdb0fe55482719"
            "67f1a67130b7105cd6a828e03909a679"
            "62e0ea1f61deb649f6bc3f4cef38c4f3"
            "5504e51ec112de5c384df7ba0b8d578a"
            "4c702b6bf11d5fac00000000"
        )
        hash_ = bytes.fromhex("3ba3edfd7a7b12b27ac72c3e67768f61"
                              "7fc81bc3888a51323a9fb8aa4b1e5e4a")

        tx = Transaction(data)

        self.assertEqual(hash_, tx.hash)
