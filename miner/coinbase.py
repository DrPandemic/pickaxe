from script import pay_pubkey_hash_script
from struct import pack
from helpers import encode_var_int


def serialize_coinbase_transaction(pubkey_hash, coinbase_data, reward):
    """
    Generates a serialized coinbase transaction to be included as a
    transaction in a mined block.

    :param pubkey_hash:   SHA256 of the public key that can claim this coinbase
                          transaction
    :param coinbase_data: data to include in the coinbase input
                          (contains the extranounce)
    :param reward:        reward (in satoshis) awarded to the miner of the
                          block that will contain this coinbase transaction
    """
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
