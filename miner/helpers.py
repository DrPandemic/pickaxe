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
