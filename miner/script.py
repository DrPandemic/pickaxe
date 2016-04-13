def pay_pubkey_hash_script(pubkey_hash):
    """
    Generates a pay-to-pubkey-hash (P2PKH) pubkey script to a given public key
    hash to be used as a TxOut script.

    :param pubkey_hash: HASH160 of the public key that can satisfy this script,
                        as internal format.
                        HASH160 is defined as RIPEMD-160(SHA-256(key)).
    :returns:           bytes of the generated pubkey script
    """
    OP_DUP = bytes([0x76])
    OP_HASH160 = bytes([0xA9])
    OP_EQUAL_VERIFY = bytes([0x88])
    OP_CHECKSIG = bytes([0xAC])

    serialized_hash = bytes([len(pubkey_hash)]) + pubkey_hash

    return (OP_DUP + OP_HASH160 +
            serialized_hash +
            OP_EQUAL_VERIFY + OP_CHECKSIG)
