import unittest

from merkle_tree import MerkleTree


class TestMerkleTree(unittest.TestCase):
    class TransactionMock:
        def __init__(self, hash_):
            self.hash = hash_

    def test_root_even_transactions(self):
        # based on the block #125552 in the mainchain
        transactions = [
            TestMerkleTree.TransactionMock(bytes.fromhex(
                "51d37bdd871c9e1f4d5541be67a6ab62"
                "5e32028744d7d4609d0c37747b40cd2d"
            )),
            TestMerkleTree.TransactionMock(bytes.fromhex(
                "60c25dda8d41f8d3d7d5c6249e2ea1b0"
                "5a25bf7ae2ad6d904b512b31f997e1a1"
            )),
            TestMerkleTree.TransactionMock(bytes.fromhex(
                "01f314cdd8566d3e5dbdd97de2d9fbfb"
                "fd6873e916a00d48758282cbb81a45b9"
            )),
            TestMerkleTree.TransactionMock(bytes.fromhex(
                "b519286a1040da6ad83c783eb2872659"
                "eaf57b1bec088e614776ffe7dc8f6d01"
            ))
        ]

        tree = MerkleTree(transactions)

        root = bytes.fromhex(
            "2b12fcf1b09288fcaff797d71e950e71ae42b91e8bdb2304758dfcffc2b620e3"
        )

        self.assertEqual(root, tree.root)

    def test_root_odd_transactions(self):
        # based on the block #125553 in the mainchain
        transactions = [
            TestMerkleTree.TransactionMock(bytes.fromhex(
                "3cfc035221a3d8eb8cdef98330467dea"
                "51ee8f75cf0cfa2fcc1bb1e150191e57"
            )),
            TestMerkleTree.TransactionMock(bytes.fromhex(
                "446e1c006bbc0d61f7fe4f6a325d468d"
                "6dd6016ace9b611370c9854e57aab0ac"
            )),
            TestMerkleTree.TransactionMock(bytes.fromhex(
                "d59ad81b484be54d97f693cfe1a5f450"
                "1948ffce13f4a558e6feb3713a1eeff6"
            )),
            TestMerkleTree.TransactionMock(bytes.fromhex(
                "6d1e61f43ec0eba4804ad74aaeff1e13"
                "7bef9bdf57098c352e6e8aeb27b95c6a"
            )),
            TestMerkleTree.TransactionMock(bytes.fromhex(
                "068b30fb5b6989bfbe0c0d5e5bca5dd9"
                "f9eb100dda21fbac0b16fed436da8f0b"
            )),
            TestMerkleTree.TransactionMock(bytes.fromhex(
                "fd48d02e10d6629d385f642879b0dbe6"
                "a12551fd011797f82dc80d56216bfcc4"
            )),
            TestMerkleTree.TransactionMock(bytes.fromhex(
                "2ec24502228833d687e9036a047f9d33"
                "880f34b237a6703c864de55a6df1013a"
            ))
        ]

        tree = MerkleTree(transactions)

        root = bytes.fromhex(
            "53fb6ea244d5f501a22c95c4c56701d70a6e115c5476ed95280cb22149c171b3"
        )

        self.assertEqual(root, tree.root)
