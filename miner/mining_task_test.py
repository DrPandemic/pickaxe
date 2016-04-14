import unittest

from mining_task import MiningTask


class MiningTaskTest(unittest.TestCase):
    def test_mining_task_ctor(self):
        coinbase_data = bytes()
        coinbase_value = 0
        # need a valid address for decoding not to fail
        wallet_address = "16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM"
        txs = []
        prev = bytes([0x42] * 32)
        bits = 0
        target = 0x4242
        time = 0x424242

        task = MiningTask(coinbase_data, coinbase_value, wallet_address, txs,
                          prev, bits, target, time)

        self.assertIsNotNone(task.block)
        # verify that coinbase tx was added to transactions
        self.assertEqual(1, len(task.block.merkle_tree.transactions))

        self.assertEqual(target, task.target)
