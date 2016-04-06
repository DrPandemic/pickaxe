#!/bin/sh
if [ $# -ne 1 ]; then
  echo "Usage:"
  echo "$0: <id>"
  exit 1
fi
args=("$@")
id=${args[0]}
bitcoin-cli -conf="../bitcoin$id.conf" -datadir="data$id" -regtest listunspent 0
