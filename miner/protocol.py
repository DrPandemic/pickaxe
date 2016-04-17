from mining_task import MiningTask
from transaction import Transaction


def parse_mining_task(template):
    """
    Parses a raw template JSON object received from the pool leader to extract
    a mining task out of it.

    :param template: template as a JSON object from the pool leader
    :returns:        MiningTask object for the block we need to work on
    """
    coinbase = bytes.fromhex(template["coinbase"])
    reward = int(template["coinbasevalue"])
    address = template["address"]
    transactions = []
    for transaction in template["transactions"]:
        serialized = bytes.fromhex(transaction["data"])
        fee = int(transaction["fee"])
        transactions.append(Transaction(serialized, fee))
    previous_block = bytes.fromhex(template["previousblockhash"])
    difficulty_bits = int(template["bits"], 16)
    target = int(template["target"], 16)
    time = int(template["curtime"])

    return MiningTask(coinbase, reward, address, transactions, previous_block,
                      difficulty_bits, target, time)


def compose_mining_result(serialized_block):
    """
    Composes a string message to send to the pool leader, containing the
    information of a mined block.

    :param serialized_block: bytes representing the serialized mined block
    :returns:                string containing the message to send to the pool
                             leader
    """
    return serialized_block.hex()
