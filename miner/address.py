from base58 import b58decode_check


def p2pkh_address_to_pubkey_hash(address):
    """
    Takes a P2PKH address (starting with a 1, m or n symbol) and extracts its
    HASH160 hash (used as a public key hash).

    :see: https://en.bitcoin.it/wiki/List_of_address_prefixes

    :param address: P2PKH public address
    :returns:       HASH160 hash of the public key
    """
    decoded = b58decode_check(address)

    # check that it is a mainnet or testnet P2PKH address
    assert(decoded[0] in [0x00, 0x6F])

    return decoded[1:]
