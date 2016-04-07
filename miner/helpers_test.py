import unittest

from helpers import to_internal_byte_order, to_rpc_byte_order, encode_var_int


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

    def test_encode_var_int_0(self):
        self.assertEqual(bytes([0]), encode_var_int(0))

    def test_encode_var_int_0xFC(self):
        self.assertEqual(bytes([0xFC]), encode_var_int(0xFC))

    def test_encode_var_int_0xFD(self):
        self.assertEqual(bytes([0xFD, 0xFD, 0x00]), encode_var_int(0xFD))

    def test_encode_var_int_0xFFFF(self):
        self.assertEqual(bytes([0xFD, 0xFF, 0xFF]), encode_var_int(0xFFFF))

    def test_encode_var_int_0x10000(self):
        expected = bytes([0xFE, 0x00, 0x00, 0x01, 0x00])
        self.assertEqual(expected, encode_var_int(0x10000))

    def test_encode_var_int_0xFFFFFFFF(self):
        expected = bytes([0xFE, 0xFF, 0xFF, 0xFF, 0xFF])
        self.assertEqual(expected, encode_var_int(0xFFFFFFFF))

    def test_encode_var_int_0x1000000000(self):
        expected = bytes([0xFF,
                          0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00])
        self.assertEqual(expected, encode_var_int(0x1000000000))
