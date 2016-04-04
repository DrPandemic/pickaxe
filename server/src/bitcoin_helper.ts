/// <reference path="typings/bitcoin-core.d.ts"/>
/// <reference path="../typings/node/node.d.ts"/>

const creds = require("./credentials.json");
import * as Client from "bitcoin-core";

export function connectToBC(): any {
  return new Client(
    {
      network: "testnet",
      username: creds.username,
      password: creds.password
    }
  );
}
