import unittest

from protocol import parse_mining_task, compose_mining_result


class ProtocolTest(unittest.TestCase):
    def test_parse(self):
        response = """
{
  "capabilities": [ "proposal" ],
  "version": 4,
  "previousblockhash": "08fc937d6edb19bc95f12f93e9fd49d83f93478c0b70ed8869fe49b289b40d9c",
  "transactions":
   [ { "data": "0100000001990ff0c35f0278c194cefb97ad8176684002b6fcd2d2c1aab41f01c8cc06b4fc0000000049483045022100c21c06c729896c42ba5217f5761718bfa858b0be9d96367fc5941c3cd6fd91540220372dfd16084e37016ed92ce2f0ea881b1b40043b42287486cdb954df6caa921f01feffffff0200ca9a3b000000001976a914f9878e9c0bc5f2021707c48b2571eab9ac550c4a88ac00196bee000000001976a91433a201e0719ca8de5cbed9d0a4313013dd54bdf788ac65000000",
       "hash": "27f28b11a2f2bf4d6b51d2b1848d5c6411a948735e21c411c4bb261ba5520cb7",
       "depends": [],
       "fee": 3840,
       "sigops": 2 } ],
  "coinbaseaux": { "flags": "" },
  "coinbasevalue": 5000003840,
  "longpollid": "08fc937d6edb19bc95f12f93e9fd49d83f93478c0b70ed8869fe49b289b40d9c105",
  "target": "7fffff0000000000000000000000000000000000000000000000000000000000",
  "mintime": 1460484636,
  "mutable": [ "time", "transactions", "prevblock" ],
  "noncerange": "00000000ffffffff",
  "sigoplimit": 20000,
  "sizelimit": 1000000,
  "curtime": 1460484709,
  "bits": "207fffff",
  "height": 102,
  "address": "mzHbFZ7xqX4yhJWyvKNCwXbNLmB21w81gd",
  "coinbase": "016600000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002f503253482f",
  "hash": "acd05af67411ca6904817cd084bd999bf8fd23473eb986d69ddbbc3aaa5f560c" }
        """

        target = (0x7fffff0 *
                  0x1000000000000000000000000000000000000000000000000000000000)
        task = parse_mining_task(response)

        self.assertEqual(target, task.target)
        self.assertIsNotNone(task.block)

    def test_compose(self):
        serialized = bytes([0x42, 0x27, 0x12])

        response = compose_mining_result(serialized)

        self.assertEqual('{"block": "422712"}', response)
