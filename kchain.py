from easy_blockchain.wallet import Wallet
from easy_blockchain.blockchain import Block, BlockChain

from sanic import Sanic
from sanic import response
from sanic_session import Session
from sanic_session import InMemorySessionInterface

import json

app = Sanic()
session = Session(app, interface=InMemorySessionInterface())
my_blockchain = None

@app.route("/")
async def welcome(request):
    return response.text('Welcome to my blockchain playground.')


@app.route("/create_wallet")
async def create_wallet(request):
    wallet = Wallet()
    public_key = wallet.getPublicKey()
    message = {
        'message': 'wallet created',
        'public key': str(public_key)
    }
    return response.json(message)


@app.route("/create_blockchain")
async def create_blockchain(request):
    my_blockchain = BlockChain()
    return response.html("<h4> New block instantiated: </h4>")


@app.route("/add_transaction", methods=['GET','POST'])
async def create_block(request):
    if request.method == 'GET':
        res = '<h4> Sorry, gotta go the post route. </h4>'
    elif request.method == 'POST':
        # create the transaction
    return response.html(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers = 1)