from bitcoin import (START_BLOCK_SUBSIDY,
                     BLOCK_SUBSIDY_HALVING_INTERVAL,
                     BLOCK_SUBSIDY_MAX_HALVINGS)
from script import pay_pubkey_hash_script
from struct import pack
from helpers import encode_var_int


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


def serialize_coinbase_transaction(pubkey_hash, coinbase_data, height,
                                   transactions):
    """
    Generates a serialized coinbase transaction to be included as a
    transaction in a mined block.

    :param pubkey_hash:   SHA256 of the public key that can claim this coinbase
                          transaction
    :param coinbase_data: data to include in the coinbase input
                          (contains the extranounce)
    :param height:        current height of the block chain, used to determine
                          the block reward
    :param transactions:  list of transactions that will be included in the
                          block of this coinbase transaction, used to determine
                          the block reward
    """
    reward = calculate_block_reward(height, transactions)
    pubkey_script = pay_pubkey_hash_script(pubkey_hash)

    VERSION = 1
    SEQUENCE = 0xFFFFFFFF

    serialized = bytearray()
    serialized.extend(pack("<I", VERSION))

    serialized.extend(encode_var_int(1))  # only 1 "input"
    serialized.extend(bytes([0] * 32))  # hash with 0s (not a transaction ref)
    serialized.extend(bytes([0xFF] * 4))  # out index with 1s
    serialized.extend(encode_var_int(len(coinbase_data)))
    serialized.extend(coinbase_data)
    serialized.extend(pack("<I", SEQUENCE))

    serialized.extend(encode_var_int(1))  # only 1 output
    serialized.extend(pack("<Q", reward))
    serialized.extend(encode_var_int(len(pubkey_script)))
    serialized.extend(pubkey_script)

    serialized.extend(pack("<I", 0))  # lock time

    return bytes(serialized)
