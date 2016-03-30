class Block:
    """
    Bitcoin block that we want to ultimately find a hash for as a miner.
    """
    VERSION = 2

    def __init__(self, previous_block_hash, merkle_tree, time, difficulty):
        self.version = Block.VERSION
        self.previous_block_hash = previous_block_hash
        self.merkle_tree = merkle_tree
        self.time = time
        self.difficulty = difficulty
        self.nounce = 0
