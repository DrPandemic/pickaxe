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
- Install an up to date node
- `npm install -g typescript`
- `npm install -g tsd`
- `npm install -g gulp`
- Inside `server/` run `tsd install` and `npm install`
### Run
- Inside `server/`, build with the command `gulp`
- Inside `server/`, run with the commande `node release/src/app.js`
