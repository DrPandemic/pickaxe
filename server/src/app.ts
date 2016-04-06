/// <reference path="typings/bitcoin-core.d.ts"/>
/// <reference path="typings/zmq.d.ts"/>

import * as Client from "bitcoin-core";
import {BlockTemplate, Template} from "./template";
import * as zmq from "zmq";
import {Server} from "./server";
const HOST: string = "tcp://127.0.0.1:";
const PORT: number = 3000;

if(process.argv[2] === "client") {
  let socket = zmq.socket("push");
  socket.connect(HOST + (PORT + 1));

  setInterval(function() {
    socket.send("02000000df11c014a8d798395b5059c722ebdf3171a4217ead71bf6e0e99f4c7000000004a6f6a2db225c81e77773f6f0457bcb05865a94900ed11356d0b75228efb38c7785d6053ffff001d005d43700101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0d03b477030164062f503253482fffffffff0100f9029500000000232103adb7d8ef6b63de74313e0cd4e07670d09a169b13e4eda2d650f529332c47646dac00000000");
  }, 1000);
} else {
  const server = new Server(HOST, PORT);
  server.start();
}
