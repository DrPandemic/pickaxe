class Transaction:
    """
    Represents a Bitcoin transaction that is contained in a block.

    In the context of a simple miner, we only care about a small subset of the
    information of a transaction.
    """
    def __init__(self, data, fees=0):
        """
        Creates a transaction.
        :param data: raw bytes of the serialized transaction
        :param fees: mining fees that can be collected from adding this
                     transaction to a mined block
        """
        self.data = data
        self.fees = fees
