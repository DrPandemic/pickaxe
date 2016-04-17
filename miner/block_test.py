import unittest

from block import Block
from helpers import to_rpc_byte_order


class TestBlock(unittest.TestCase):
    class MerkleTreeMock:
        def __init__(self):
            self.root = bytes([42] * 32)
            self.transactions = []

    class TransactionMock:
        def __init__(self, data):
            self.data = data

    def test_init(self):
        prev = bytes([123] * 32)
        tree = TestBlock.MerkleTreeMock()
        time = 432432
        bits = 0x1a44b9f2
        nounce = None

        b = Block(prev, tree, time, bits)

        self.assertEqual(prev, b.previous_block_hash)
        self.assertEqual(Block.VERSION, b.version)
        self.assertEqual(tree, b.merkle_tree)
        self.assertEqual(time, b.time)
        self.assertEqual(bits, b.difficulty)
        self.assertEqual(nounce, b.nounce)

    def test_serialize_header(self):
        # example taken from:
        # https://bitcoin.org/en/developer-reference#block-headers
        tree = TestBlock.MerkleTreeMock()
        tree.root = to_rpc_byte_order(bytes.fromhex(
            "9d10aa52ee949386ca9385695f04ede270dda20810decd12bc9b048aaab31471"
        ))
        prev = to_rpc_byte_order(bytes.fromhex(
            "b6ff0b1b1680a2862a30ca44d346d9e8910d334beb48ca0c0000000000000000"
        ))
        time = 0x545ad924
        target = 0x181bc330
        nounce = 0x64089ffe

        b = Block(prev, tree, time, target)
        b.nounce = nounce

        header = bytes.fromhex(
            "04000000"
            "b6ff0b1b1680a2862a30ca44d346d9e8910d334beb48ca0c0000000000000000"
            "9d10aa52ee949386ca9385695f04ede270dda20810decd12bc9b048aaab31471"
            "24d95a54"
            "30c31b18"
            "fe9f0864"
        )

        self.assertEqual(header, b.serialize_header())

    def test_serialize_header_unsigned_ints(self):
        """
        Verifies that we support high nounces.
        """
        tree = TestBlock.MerkleTreeMock()
        prev = to_rpc_byte_order(bytes([12] * 32))
        time = 0x12121212
        target = 0x12121212
        nounce = 0xFFFFFFFF

        b = Block(prev, tree, time, target)
        b.nounce = nounce

        b.serialize_header()
        # no exception raised -> success

    def test_serialize_block(self):
        # example taken from:
        # https://bitcoin.org/en/developer-reference#submitblock
        tree = TestBlock.MerkleTreeMock()
        tree.root = to_rpc_byte_order(bytes.fromhex(
            "4a6f6a2db225c81e77773f6f0457bcb05865a94900ed11356d0b75228efb38c7"
        ))
        prev = to_rpc_byte_order(bytes.fromhex(
            "df11c014a8d798395b5059c722ebdf3171a4217ead71bf6e0e99f4c700000000"
        ))
        time = 0x53605d78
        target = 0x1d00ffff
        nounce = 0x70435d00
        transactions = [TestBlock.TransactionMock(bytes.fromhex(
            "0100000001000000000000000000000000000000000000000000000000000"
            "0000000000000ffffffff0d03b477030164062f503253482fffffffff0100"
            "f9029500000000232103adb7d8ef6b63de74313e0cd4e07670d09a169b13e"
            "4eda2d650f529332c47646dac00000000"
        ))]
        tree.transactions = transactions

        block = Block(prev, tree, time, target)
        block.nounce = nounce

        serialized = bytes.fromhex(
            "04000000df11c014a8d798395b5059c"
            "722ebdf3171a4217ead71bf6e0e99f4"
            "c7000000004a6f6a2db225c81e77773"
            "f6f0457bcb05865a94900ed11356d0b"
            "75228efb38c7785d6053ffff001d005"
            "d437001010000000100000000000000"
            "0000000000000000000000000000000"
            "0000000000000000000ffffffff0d03"
            "b477030164062f503253482ffffffff"
            "f0100f9029500000000232103adb7d8"
            "ef6b63de74313e0cd4e07670d09a169"
            "b13e4eda2d650f529332c47646dac00"
            "000000"
        )

        self.assertEqual(serialized, block.serialize())
