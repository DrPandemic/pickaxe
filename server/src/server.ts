/// <reference path="bitcoin-core.d.ts"/>
/// <reference path="../typings/node/node.d.ts"/>
const creds = require("./credentials.json");
import * as Client from "bitcoin-core";
import Template from "./template";

const client = new Client(
  {
    network: "testnet",
    username: creds.username,
    password: creds.password
  }
);

client.getBlockTemplate()
.then((results:any) => {
  let template:Template = new Template(results);
  console.log(template);
}).catch((error:any) => {
  console.error(error);
});
