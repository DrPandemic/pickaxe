#!/bin/sh
if [ $# -ne 2 ]; then
  echo "Usage:"
  echo "$0: <source id> <destination address>"
  exit 1
fi

args=("$@")
id=${args[0]}
address=${args[1]}

bitcoin-cli -conf="../bitcoin$id.conf" -datadir="data$id" -regtest  sendtoaddress $address 10.00
