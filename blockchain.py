
from block import Block

class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """
    def __init__(self):
        self.chain = []

    def add_block(self, data):
        self.chain.append(Block(data))

    def __repr__(self) -> str:
        return f'Blockchain: {self.chain}'


blockchain = Blockchain()
blockchain.add_block('first')
blockchain.add_block('second')

print(blockchain)