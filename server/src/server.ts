/// <reference path="bitcoin-core.d.ts"/>
/// <reference path="../typings/node/node.d.ts"/>
import * as Client from "bitcoin-core";
const creds = require("./credentials.json");

const client = new Client(
  {
    network: "testnet",
    username: creds.username,
    password: creds.password
  }
);

client.getBlockTemplate()
.then((results:any) => {
  console.log(results);
}).catch((error:any) => {
  console.error(error);
});
