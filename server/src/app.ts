/// <reference path="typings/bitcoin-core.d.ts"/>
/// <reference path="typings/zmq.d.ts"/>

import * as Client from "bitcoin-core";
import {BlockTemplate, Template} from "./template";
import * as zmq from "zmq";
import {connectToBC} from "./bitcoin_helper"
import {Server, Message, MessageTypes} from "./server";
const ADDRESS: string = "tcp://127.0.0.1:3000";

/*function testZmq(type_: zmq.types) {
  let sock = zmq.socket(type_);
  switch(type_) {
    case "push":
      sock.bindSync("tcp://127.0.0.1:3000");
      sock.send(JSON.stringify({1:5}));
    break;
    case "pull":
      sock.connect("tcp://127.0.0.1:3000");
      sock.on("message", function(msg: any){
        console.log('work: %s', msg.toString());
      });
    case "pub":
      sock.bindSync("tcp://127.0.0.1:3000");
      sock.send(JSON.stringify({1:5}));
      setInterval(() => {
        sock.send(JSON.stringify({some_nice: "jewellery"}));
      }, 1000);
    break;
    default:
      throw new Error();
  }
}*/

/*
client.getBlockTemplate()
.then((results:BlockTemplate) => {
  let template:Template = new Template(results);
  console.log(template);
}).catch((error:any) => {
  console.error(error);
}); */


if(process.argv[2] === "client") {
  let msg = Message.make({type_: MessageTypes.Connection, data: {1:2}});
  let sock = zmq.socket("push");
  sock.bindSync(ADDRESS);
  console.log(JSON.stringify(msg));
  sock.send(JSON.stringify(msg));
  console.log("sent");
} else {
  const client = connectToBC();
  const server = new Server(ADDRESS);
  server.start();
}
