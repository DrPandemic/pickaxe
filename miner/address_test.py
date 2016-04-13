import unittest

from address import p2pkh_address_to_pubkey_hash


class AddressTest(unittest.TestCase):
    def test_address_p2pkh_to_pubkey_hash_mainnet(self):
        # taken from:
        # https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses
        addr = "16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM"
        expected = bytes.fromhex(
            "010966776006953D5567439E5E39F86A0D273BEE"
        )

        hash_ = p2pkh_address_to_pubkey_hash(addr)

        self.assertEqual(expected, hash_)
