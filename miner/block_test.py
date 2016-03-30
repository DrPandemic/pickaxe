import unittest

from block import Block


class TestBlock(unittest.TestCase):
    class MerkleTreeMock:
        pass

    def test_init(self):
        prev = 0x123123
        tree = TestBlock.MerkleTreeMock()
        time = 0x432432
        bits = 0x1a44b9f2

        b = Block(prev, tree, time, bits)

        self.assertEqual(b.previous_block_hash, prev)
        self.assertEqual(b.version, Block.VERSION)
        self.assertEqual(b.merkle_tree, tree)
        self.assertEqual(b.time, time)
        self.assertEqual(b.difficulty, bits)
