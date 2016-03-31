from hashlib import sha256


def mine(block, target, start=0, end=0xFFFFFFFF):
    for nounce in range(start, end+1):
        block.nounce = nounce
        header = block.serialize_header()
        hash_ = sha256(sha256(header).digest()).digest()

        value = int.from_bytes(hash_, byteorder='little', signed=False)

        if value <= target:
            return

    block.nounce = None
