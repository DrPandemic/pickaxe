from struct import pack


def to_internal_byte_order(rpc_byte_order):
    """
    Returns a given RPC byte order hash (bytes) to the format expected by
    Bitcoin primitives (blocks, transactions, etc.)
    """
    return rpc_byte_order[::-1]


def to_rpc_byte_order(internal_byte_order):
    """
    Returns a given internal byte order hash (bytes) to the format expected by
    the RPC client.
    """
    return internal_byte_order[::-1]


def encode_var_int(n):
    """
    Encodes an unsigned integer as a variable integer format.

    See:
    https://en.bitcoin.it/wiki/Protocol_documentation#Variable_length_integer
    """

    if n < 0xFD:
        return pack("<B", n)
    elif n <= 0xFFFF:
        return bytes([0xFD]) + pack("<H", n)
    elif n <= 0xFFFFFFFF:
        return bytes([0xFE]) + pack("<I", n)
    else:
        return bytes([0xFF]) + pack("<Q", n)
