from flask import Flask
from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

# adding temp code to view on our running app
for i in range(3):
    blockchain.add_block(i)

# endpoints

@app.route('/')
def default():
    return 'Welcome to the Blockchain'


@app.route('/blockchain')
def route_blockchain():
    # cannot just return an instance of the chain because of its data type
    # instead return the helper function that stringifies the chain for us
    return blockchain.__repr__()


app.run()