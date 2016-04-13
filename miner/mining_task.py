class MiningTask:
    """
    Takes the raw data obtained from 
    """
    def __init__(self, coinbase_data, coinbase_value, wallet_address,
                 transactions, previous_block_hash, target):
        """
        TODO
        """
        self.coinbase = coinbase_data
        self.block_reward = coinbase_value
        self.address = wallet_address
        self.transactions = transactions
        self.previous_block = previous_block_hash
        self.target = target
