from proof_of_work import ProofOfWork


class Node:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.peers = []  # This would be a list of other nodes in the network in a real blockchain

    def add_block(self, block):
        proof = ProofOfWork.proof_of_work(block)
        added = self.blockchain.add_block(block, proof)
        return added
