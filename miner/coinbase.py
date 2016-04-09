from bitcoin import (START_BLOCK_SUBSIDY,
                     BLOCK_SUBSIDY_HALVING_INTERVAL,
                     BLOCK_SUBSIDY_MAX_HALVINGS)


def calculate_block_reward(height, transactions):
    """
    Calculates the amount of satoshis that can be spent from a coinbase
    transaction.

    This depends on the amount of satoshis mined (based on current height)
    and transaction fees included in the mined block.

    :param height:         current height of the blockchain
    :param transactions:   transactions included in the mined block
    :returns:              reward (in satoshis) produced by the coinbase
                           transaction
    """
    halvings = height // BLOCK_SUBSIDY_HALVING_INTERVAL
    fees = sum(tx.fees for tx in transactions)

    if halvings >= BLOCK_SUBSIDY_MAX_HALVINGS:
        return fees

    reward = START_BLOCK_SUBSIDY >> halvings

    return reward + fees


def serialize_coinbase_transaction(miner_address, height, transactions):
    pass
