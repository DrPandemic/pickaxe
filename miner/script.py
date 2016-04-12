def pay_pubkey_hash_script(pubkey_hash):
    """
    Generates a pay-to-pubkey-hash (P2PKH) pubkey script to a given public key
    hash to be used as a TxOut script.

    :param pubkey_hash: SHA256 of the public key that can satisfy this script,
                        as internal format
    :returns:           bytes of the generated pubkey script
    """
    OP_DUP = bytes([0x76])
    OP_SHA256 = bytes([0xA8])
    OP_EQUAL_VERIFY = bytes([0x88])
    OP_CHECKSIG = bytes([0xAC])

    serialized_hash = bytes([len(pubkey_hash)]) + pubkey_hash

    return OP_DUP + OP_SHA256 + serialized_hash + OP_EQUAL_VERIFY + OP_CHECKSIG
