import unittest

from block import Block
from cpu_miner import mine


class TestCpuMiner(unittest.TestCase):
    # Based on 00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d
    # (block at height 125552 in Mainchain)
    class MerkleTreeMock:
        def __init__(self):
            self.root = bytes.fromhex(
                "2b12fcf1b09288fcaff797d71e950e71"
                "ae42b91e8bdb2304758dfcffc2b620e3"
            )
    target = 0x44b9f20000000000000000000000000000000000000000000000

    def _fake_block(self):
        prev = bytes.fromhex(
            "00000000000008a3a41b85b8b29ad444def299fee21793cd8b9e567eab02cd81"
        )
        tree_mock = TestCpuMiner.MerkleTreeMock()
        block = Block(prev, tree_mock, 0x4dd7f5c7, 0x1a44b9f2)
        block.version = 1
        return block

    def test_mine_successful(self):
        nounce = 0x9546a142
        block = self._fake_block()

        mine(block, TestCpuMiner.target,
             start=nounce-100, end=nounce+100)
        self.assertEqual(nounce, block.nounce)

    def test_mine_unsuccessful(self):
        bad_nounce = 0x12121212
        block = self._fake_block()
        block.nounce = bad_nounce

        mine(block, TestCpuMiner.target,
             start=bad_nounce, end=bad_nounce)
        self.assertEqual(None, block.nounce)
