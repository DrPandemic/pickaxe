from coinbase import serialize_coinbase_transaction
from address import p2pkh_address_to_pubkey_hash
from transaction import Transaction
from merkle_tree import MerkleTree
from block import Block


class MiningTask:
    """
    Takes the raw data obtained from a pool server mining request and stores
    it. Can produce a mineable block from the raw data.
    """
    def __init__(self, coinbase_data, coinbase_value, wallet_address,
                 transactions, previous_block_hash, difficulty_bits,
                 target, time):
        """
        Takes the given raw data from a mining request and produces a mineable
        block accessible from the attribute `block`.

        The target hash value will be held in the attribute `target`.

        :param coinbase_data:       data to include as a script to the TxIn of
                                    the coinbase transaction
        :param coinbase_value:      Reward for mining this block.
                                    This value should contain the block subsidy
                                    (based on height of the blockchain) plus
                                    the fees of the included `transactions`.
        :param wallet_address:      address that will receive the bitcoins
                                    mined (through the coinbase transaction)
        :param transactions:        transactions that we want to put in the
                                    mineable block
        :param previous_block_hash: hash (RPC format) of the previous block
        :param difficulty_bits:     packed representation (bits) of the current
                                    network's difficulty as an integer
        :param target:              target value for the mining task, which
                                    indicates that we must mine a block that
                                    hashes to a value below that target
        :param time:                unix time since epoch in seconds
        """
        pubkey = p2pkh_address_to_pubkey_hash(wallet_address)
        coinbase = serialize_coinbase_transaction(pubkey, coinbase_data,
                                                  coinbase_value)
        coinbase_tx = Transaction(coinbase)
        transactions = [coinbase_tx] + transactions
        tree = MerkleTree(transactions)

        self.target = target
        self.block = Block(previous_block_hash, tree, time, difficulty_bits)
