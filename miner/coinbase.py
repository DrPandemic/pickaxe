from bitcoin import (START_REWARD, REWARD_MAX_HALVINGS,

                     REWARD_HALVING_INTERVAL)


def calculate_coinbase_value(height, transactions):
    """
    Calculates the amount of satoshis that can be spent from a coinbase
    transaction.

    This depends on the amount of satoshis mined (based on current height)
    and transaction fees included in the mined block.

    :param height:         current height of the blockchain
    :param transactions:   transactions included in the mined block
    :returns:              amount of satoshis produced by the coinbase
                           transaction
    """
    halvings = height // REWARD_HALVING_INTERVAL
    fees = sum(tx.fees for tx in transactions)

    if halvings >= REWARD_MAX_HALVINGS:
        return fees

    reward = START_REWARD >> halvings

    return reward + fees
