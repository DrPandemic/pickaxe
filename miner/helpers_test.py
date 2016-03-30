import unittest

from helpers import to_internal_byte_order, to_rpc_byte_order


class TestHelpers(unittest.TestCase):
    rpc_order = bytes.fromhex(
        "5472ac8b1187bfcf91d6d218bbda1eb2405d7c55f1f8cc820000000000000000"
    )
    internal_byte_order = bytes.fromhex(
        "000000000000000082ccf8f1557c5d40b21edabb18d2d691cfbf87118bac7254"
    )

    def test_to_internal_byte_order(self):
        internal_byte_order = to_internal_byte_order(TestHelpers.rpc_order)
        self.assertEqual(TestHelpers.internal_byte_order, internal_byte_order)

    def test_to_rpc_byte_order(self):
        rpc_order = to_rpc_byte_order(TestHelpers.internal_byte_order)
        self.assertEqual(TestHelpers.rpc_order, rpc_order)
