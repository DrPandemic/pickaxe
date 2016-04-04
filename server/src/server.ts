/// <reference path="typings/bitcoin-core.d.ts"/>
/// <reference path="typings/zmq.d.ts"/>
/// <reference path="../typings/node/node.d.ts"/>

const creds = require("./credentials.json");
import * as Client from "bitcoin-core";
import {BlockTemplate, Template} from "./template";
import * as zmq from "zmq";

function testZmq(type_: zmq.types) {
  let sock = zmq.socket(type_);
  switch(type_) {
    case "push":
      sock.bindSync("tcp://127.0.0.1:3000");
      sock.send("some work");
      break;
    case "pull":
      sock.connect("tcp://127.0.0.1:3000");
      sock.on("message", function(msg: any){
        console.log('work: %s', msg.toString());
      });
    case "pub":
      break;
    case "sub":
      break;
    default:
      throw new Error();
  }
}

function testBitcoin() {
  const client = new Client(
    {
      network: "testnet",
      username: creds.username,
      password: creds.password
    }
  );

  client.getBlockTemplate()
  .then((results:BlockTemplate) => {
    let template:Template = new Template(results);
    console.log(template);
  }).catch((error:any) => {
    console.error(error);
  });
}

testZmq(<zmq.types>process.argv[2] || "push");
