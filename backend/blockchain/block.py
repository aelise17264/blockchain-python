import time
from backend.util.crypto_hash import crypto_hash
from backend.util.hex_to_binary import hex_to_binary
from backend.config import MINE_RATE

GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': 'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': [],
    'difficulty': 3,
    'nonce': 'genesis_nonce'
}

class Block:
    """
    Block - unit of storage.
    Store transactions in a blockchain that supports crypto
    """
    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self) -> str:
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data}, '
            f'difficulty: {self.difficulty}, '
            f'nonce: {self.nonce} )'
            )
    
    @staticmethod
    def mine_block(last_block, data):
        """
        Mines a block based on the given last_block & data, 
        until a block hash is found that meets the leading 0's proof of work requirment.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = Block.adjust_difficulty(last_block, timestamp)
        nonce = 0
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)
    
        # to make sure the has begins with the correct number of leading 0's
        while hex_to_binary(hash)[0:difficulty] != '0' * difficulty:
            nonce += 1
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(last_block, timestamp)
            # re run difficulty here to make sure it's based on the most accurate timestamp available
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)


        return Block(timestamp, last_hash, hash, data, difficulty, nonce)

    @staticmethod
    def genesis():
        """
        generate the genesis block to begin the chain
        """
        return Block(**GENESIS_DATA)
        # return Block(
        #     GENESIS_DATA['timestamp'],
        #     GENESIS_DATA['last_hash'],
        #     GENESIS_DATA['hash'],
        #     GENESIS_DATA['data']
        # )

    @staticmethod
    def adjust_difficulty(last_block, new_timestamp):
        """
        this will calculate the adjusted difficulty according to the MINE_RATE
        Increase the difficulty for blocks mined too quickly
        Decrease the difficulty for blooks mined too slowly
        """
        if(new_timestamp - last_block.timestamp) < MINE_RATE:
            return last_block.difficulty + 1
        
        if(last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1

        return 1
    
    @staticmethod
    def is_valid_block(last_block, block):

        if block.last_hash != last_block.hash:
            raise Exception('The block last_hash must be correct')
        
        if hex_to_binary(block.hash)[0:block.difficulty] != '0' * block.difficulty:
            raise Exception('The proof of work requirement was not met')
        
        if abs(last_block.difficulty - block.difficulty) > 1:
            raise Exception('The block difficulty must only adjust by 1')
        
        reconstructed_hash = crypto_hash(
            block.timestamp,
            block.last_hash,
            block.data,
            block.nonce,
            block.difficulty
        )

        if block.hash != reconstructed_hash:
            raise Exception('The block has must be correct')



def main():
    genesis_block = Block.genesis()
    bad_block = Block.mine_block(genesis_block, 'start')
    # bad_block.last_hash = 'problem_child'
    try:
        Block.is_valid_block(genesis_block, bad_block)
        print('success')
    except Exception as e:
        print(f'is valid block: {e}')
    # block = Block('blockparty')
    # print(block)
    # print(f'block.py __name__: {__name__}')

    # genesis_block = Block.genesis()
    # block = Block.mine_block(genesis_block, 'start')
    # print(block)

if __name__ == "__main__":
    main()