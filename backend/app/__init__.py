from flask import Flask, jsonify
from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

# adding temp code to view on our running app
# for i in range(3):
#     blockchain.add_block(i)

# endpoints

@app.route('/')
def default():
    return 'Welcome to the Blockchain'


@app.route('/blockchain')
def route_blockchain():
    # cannot just return an instance of the chain because of its data type
    # use flask's jsonify to return a JSON response from our blockchain
    return jsonify(blockchain.to_json())
    
    # instead return the helper function that stringifies the chain for us
    # return blockchain.__repr__()

@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction_data = 'test_transaction_data'
    blockchain.add_block(transaction_data)

    return jsonify(blockchain.chain[-1].to_json())

app.run()