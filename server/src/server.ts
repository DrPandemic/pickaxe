/// <reference path="bitcoin-core.d.ts"/>
/// <reference path="../typings/node/node.d.ts"/>
import * as Client from "bitcoin-core";
let creds = require("./credentials.json");

const client = new Client({
                network: "testnet",
                username: creds.username,
                password: creds.password
              });

console.log(client.getBlockTemplate());
