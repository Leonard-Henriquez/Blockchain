from Functions import *
import json


class Blockchain( object ):
    def __init__(self):
        self.current_transactions = []
        block = {
            'index': 0,
            'timestamp': timestamp(),
            'transactions': [],
            'nonce': 0,
            'previous_block_hash': 0,
        }
        self.blockchain = [block]
        pass

    def mine(self, miner_address):
        """Create a new block"""

        coinbase = [{
            'sender': -1,
            'receiver': miner_address,
            'amount': 1000,
        }]

        # validate transactions

        transactions = coinbase + self.current_transactions

        # find nonce with Proof of Work

        # propose new block to the blockchain
        nonce = 0
        block = {
            'index': len( self.blockchain ),
            'timestamp': timestamp(),
            'transactions': transactions,
            'nonce': nonce,
            'previous_block_hash': self.last_block_hash,
        }
        self.blockchain.append( block )
        self.current_transactions = []
        return block

    def transfer(self, sender_address, receiver_address, amount):
        """Create a new transaction"""
        self.current_transactions.append( {
            'sender': sender_address,
            'receiver': receiver_address,
            'amount': amount,
        } )
        return self.current_transactions

    def check_balance(self, address):
        def amounts():
            for block in self.blockchain:
                for transaction in block['transactions']:
                    if transaction['receiver'] == address:
                        yield transaction['amount']
                    elif transaction['sender'] == address:
                        yield -transaction['amount']

        balance = 0
        for amount in amounts():
            balance += amount
        return balance

    @property
    def last_block(self):
        """Last block"""
        return self.blockchain[-1]

    @property
    def last_block_hash(self):
        block = self.last_block
        block_string = json.dumps( block, sort_keys=True ).encode()
        return hash( block_string )
