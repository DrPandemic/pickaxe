from hashlib import sha256


def mine(block, target, start=0, end=0xFFFFFFFF):
    """
    Searches the nounce integer space ([start,end]) for one that will produce a
    block with a hash under the given target.

    If a valid hash is found, `block.nounce` will contain the nounce that
    produces that hash.
    If none is found, `block.nounce` will be `None`.

    :param block:  Block that we want a valid hash for.
                   `block.nounce` will contain the found hash (or None).
    :param target: Target value for the hash as an integer. If a hash is found,
                   it will be less than equal that value.
    :param start:  starting value for the nounce search
    :param end:    final value for the nounce search
    """
    assert(end >= start)
    for nounce in range(start, end+1):
        block.nounce = nounce
        header = block.serialize_header()
        hash_ = sha256(sha256(header).digest()).digest()

        value = int.from_bytes(hash_, byteorder='little', signed=False)

        if value <= target:
            return

    block.nounce = None
