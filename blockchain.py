import time
from block import Block
from proof_of_work import ProofOfWork

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.unconfirmed_transactions = []

    def create_genesis_block(self):
        return Block(0, [], time.time(), "0")

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def add_block(self, block, proof):
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash or not self.is_valid_proof(block, proof):
            return False
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        return block_hash.startswith('0000') and block_hash == block.compute_hash()

    @property
    def last_block(self):
        return self.chain[-1]
