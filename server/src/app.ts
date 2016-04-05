/// <reference path="typings/bitcoin-core.d.ts"/>
/// <reference path="typings/zmq.d.ts"/>

import * as Client from "bitcoin-core";
import {BlockTemplate, Template} from "./template";
import * as zmq from "zmq";
import {Server, Message, MessageTypes} from "./server";
const ADDRESS: string = "tcp://127.0.0.1:3000";

if(process.argv[2] === "client") {
  let sock = zmq.socket("sub");
  sock.connect(ADDRESS);
  sock.subscribe("");
  console.log(45);
  sock.on('message', function(data:any) {
    console.log(85);
    console.log(data.toString());
  });
} else {
  const server = new Server(ADDRESS);
  server.start();
}
