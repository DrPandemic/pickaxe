from hashlib import sha256

from helpers import to_internal_byte_order, to_rpc_byte_order


class MerkleTree:
    """
    Merkle tree of the transactions in a block.

    This is a tree that combines the hashes of the
    transactions together until it reaches a single
    hash: the merkle root.
    """
    def __init__(self, transactions):
        """
        Creates a merkle tree out of a list of transactions.

        :param transactions: The list of transactions in the tree.
                             The first transaction in the list should be the
                             coinbase transaction.
        """
        hashes = list(map(lambda t: to_internal_byte_order(t.hash),
                          transactions))
        self.root = to_rpc_byte_order(self._build_tree(hashes))

    def _build_tree(self, hashes):
        """
        Builds a merkle tree out of a list of transaction hashes.

        :param hashes: list of transaction hashes (txids)
        :returns:      the computed root of the merkle tree
        """
        assert(hashes)

        # if we have our root hash, we're done
        if len(hashes) == 1:
            return hashes[0]

        # odd number of hashes? duplicate the last element
        if len(hashes) % 2 == 1:
            hashes.append(hashes[-1])

        trees = []
        for i in range(0, len(hashes), 2):
            combined = hashes[i] + hashes[i + 1]
            hashed = sha256(sha256(combined).digest()).digest()
            trees.append(hashed)

        return self._build_tree(trees)
