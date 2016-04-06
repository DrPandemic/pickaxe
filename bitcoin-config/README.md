# Create your own small bitcoin network
## Init
You need to have ```bitcoind``` and ```bitcoin-cli``` installed.

To start the network run ```./start.sh``` and to stop it run ```./stop.sh```

## Making money
You can run ```./generate-bitcoins.sh``` to generate 101 bitcoins owned by
user 2.

If you want to make a transaction get the address of the receiver by running
```./get-address 3```. After, run ```./generate-transaction.sh 2 the_address```.

If you wait an instant (remember the network is not instantaneous, you should
see some unconfirmed bitcoins with ```./get-bitcoins.sh 3```.
