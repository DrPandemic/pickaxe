import unittest

from script import pay_pubkey_hash_script


class ScriptTest(unittest.TestCase):
    def test_create_P2PKH_pubkey_script_generation(self):
        # taken from:
        # https://en.bitcoin.it/wiki/Script#Standard_Transaction_to_Bitcoin_address_.28pay-to-pubkey-hash.29
        hash_ = bytes.fromhex(
            "89ABCDEFABBAABBAABBAABBAABBAABBAABBAABBA"
        )
        expected = bytes.fromhex(
            "76A91489ABCDEFABBAABBAABBAABBAABBAABBAABBAABBA88AC"
        )

        self.assertEqual(expected, pay_pubkey_hash_script(hash_))
