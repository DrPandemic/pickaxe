# Pickaxe
Bitcoin Mining Pool

[![Build Status](https://travis-ci.org/DrPandemic/pickaxe.svg?branch=master)](https://travis-ci.org/DrPandemic/pickaxe)
[![Coverage Status](https://coveralls.io/repos/github/DrPandemic/pickaxe/badge.svg?branch=coveralls)](https://coveralls.io/github/DrPandemic/pickaxe?branch=coveralls)
[![Code Climate](https://codeclimate.com/github/DrPandemic/pickaxe/badges/gpa.svg)](https://codeclimate.com/github/DrPandemic/pickaxe)

## Bitcoind
- Install bitcoind on your system
- Inside `bitcoin-config/`, run `./start.sh`

## Miner
### Install
`make install` (possibly requires `sudo`)
### Run tests
- Unit tests: `make test`
- Unit tests with branch coverage: `make coverage`

## Server
### Install
- Install the system library `zeromq`
- Install an up-to-date node
- `npm install -g typescript`
- `npm install -g tsd`
- `npm install -g gulp`
- Inside `server/` run `tsd install` and `npm install`
### Run
- Inside `server/`, build with the command `gulp`
- Inside `server/`, run with the commande `node release/src/app.js`

## Example Usage
Let's run through a full example of setting up the network and using the pool
leader & miners.

### Starting the Network
```
> cd bitcoin-config
> ./start.sh
```

Taking a look at our 2nd user, we see that he has no bitcoins:
```
> ./get-balance.sh 2
0.00000000
```

Let's give him some.
```
> ./generate-bitcoins.sh
> ./get-balance.sh 2
50.00000000
```
Note: `generate-bitcoins` mined 101 blocks. The reason why our 2nd user only has
50 bitcoins is because [mined block rewards need to mature before they can be spent](http://bitcoin.stackexchange.com/a/10831).
As new blocks are mined, the rewards from the other 100 blocks will be added to
our 2nd user's balance.

### Starting the Server
In another terminal, run the following:
```
> cd server
> gulp

... wait until it is done, then Ctrl+C

> node release/app.js
```

### Starting a Miner
In another terminal, run the following:
```
> python miner.py
```
Sit back, and enjoy watching the blocks getting mined.

Let's see if our 3rd user is getting rich (in the `bitcoind-config` terminal):
```
> ./get-balance.sh 3
1850.00000000

...

> ./get-balance.sh 3
8368.75000000
```

:tada:

### Adding a Transaction
We can add a transaction to the network and our miner will properly add it to a
block that it mines (in the `bitcoind-config` terminal):
```
> ./get-balance.sh 1
0.00000000

> ./get-address.sh 1
...
    "address": "mgAEr5mT9ZhWgXxNqeYWXYbdahdY82PZce",
...

> ./generate-transaction.sh 3 mgAEr5mT9ZhWgXxNqeYWXYbdahdY82PZce

> ./get-balance.sh 1
10.00000000
```
