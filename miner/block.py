from struct import pack

from helpers import to_internal_byte_order


class Block:
    """
    Bitcoin block that we want to ultimately find a hash for as a miner.
    """
    VERSION = 2

    def __init__(self, previous_block_hash, merkle_tree, time, difficulty):
        """
        Creates a Bitcoin block.

        :param previous_block_hash: hash (RPC byte order) of the previous block
                                    in the blockchain
        :param merkle_tree:         merkle tree of the transactions in the
                                    block
        :param time:                Unix time since epoch in seconds
        :param difficulty:          Packed representation (bits) of the current
                                    network's difficulty
        """
        self.version = Block.VERSION
        self.previous_block_hash = previous_block_hash
        self.merkle_tree = merkle_tree
        self.time = time
        self.difficulty = difficulty
        self.nounce = 0

        assert(len(self.previous_block_hash) == 32)
        assert(len(self.merkle_tree.root) == 32)

    def serialize_header(self):
        """
        Serializes the header of the block to a bytes object.

        This is the chunk of bytes that we want to hash in our search for a
        valid hash.
        """
        return (pack("<i", self.version) +
                to_internal_byte_order(self.previous_block_hash) +
                to_internal_byte_order(self.merkle_tree.root) +
                pack("<i", self.time) +
                pack("<i", self.difficulty) +
                pack("<i", self.nounce))
