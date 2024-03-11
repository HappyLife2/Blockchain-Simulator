import time
from blockchain import Blockchain
from block import Block
from proof_of_work import ProofOfWork
from transaction import Transaction

# Initialize blockchain
blockchain = Blockchain()

# Create a new transaction and add it to the blockchain
transaction = Transaction("Alice", "Bob", 100)
blockchain.add_new_transaction(transaction.to_dict())

# Mine a new block
previous_block = blockchain.last_block
new_block = Block(index=previous_block.index + 1,
                  transactions=blockchain.unconfirmed_transactions,
                  timestamp=time.time(),
                  previous_hash=previous_block.hash)
proof = ProofOfWork.proof_of_work(new_block)
blockchain.add_block(new_block, proof)

print("Blockchain:")
for block in blockchain.chain:
    print(block.__dict__)
