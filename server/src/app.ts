/// <reference path="typings/bitcoin-core.d.ts"/>
/// <reference path="typings/zmq.d.ts"/>

import {Server} from "./server";
const HOST: string = "tcp://127.0.0.1:";
const PORT: number = 8080;

const server = new Server(HOST, PORT);
server.start();
