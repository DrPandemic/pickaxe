/// <reference path="typings/bitcoin-core.d.ts"/>
/// <reference path="../typings/node/node.d.ts"/>

const creds = require("./credentials.json");
import * as Client from "bitcoin-core";

export function connectToBC(): any {
  return new Client(
    {
      network: "regtest",
      username: "username",
      password: "password",
      port: 16593
    }
  );
}
