import unittest

from block import Block
from helpers import to_rpc_byte_order


class TestBlock(unittest.TestCase):
    class MerkleTreeMock:
        def __init__(self):
            self.root = bytes([42] * 32)

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
            "02000000"
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
