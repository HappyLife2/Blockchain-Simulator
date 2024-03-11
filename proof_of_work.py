class ProofOfWork:
    @staticmethod
    def proof_of_work(block):
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0000'):  # Adjust difficulty with the number of leading zeros
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash
