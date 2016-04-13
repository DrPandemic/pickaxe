import json

from mining_task import MiningTask
from transaction import Transaction


def parse_mining_task(response):
    """
    Parses a raw string received from the pool leader to extract a mining task.

    :param response: string received from the pool leader
    :returns:        MiningTask object for the block we need to work on
    """
    data = json.loads(response)

    coinbase = bytes.fromhex(data["coinbase"])
    reward = int(data["coinbasevalue"])
    address = data["address"]
    transactions = []
    for transaction in data["transactions"]:
        serialized = bytes.fromhex(transaction["data"])
        fee = int(transaction["fee"])
        transactions.append(Transaction(serialized, fee))
    previous_block = bytes.fromhex(data["previousblockhash"])
    difficulty_bits = int(data["bits"], 16)
    target = int(data["target"], 16)
    time = int(data["curtime"])

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
    block = ''.join('{:02x}'.format(byte) for byte in serialized_block)
    response = {'block': block}

    return json.dumps(response)
