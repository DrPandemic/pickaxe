from hashlib import sha256


class Transaction:
    """
    Represents a Bitcoin transaction that is contained in a block.

    In the context of a simple miner, we only care about a small subset of the
    information of a transaction.
    """
    def __init__(self, data, fee=0):
        """
        Creates a transaction.
        :param data: raw bytes of the serialized transaction
        :param fee:  mining fee that can be collected from adding this
                     transaction to a mined block
        """
        self.data = data
        self.hash = sha256(sha256(data).digest()).digest()
        self.fee = fee
