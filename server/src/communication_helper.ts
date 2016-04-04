/// <reference path="typings/zmq.d.ts"/>
/// <reference path="../typings/node/node.d.ts"/>

import * as zmq from "zmq";
const assert = require('assert');

export enum MessageTypes {
  Connection,
  Disctionnection,
  NewTemplate,
  Submit
}

export class Message {
  "type": MessageTypes;
  data: any;

  static make(data:any): Message {
    assert(typeof data["type"] === "number");
    assert(typeof data.data !== "undefined");
    assert(Object.keys(MessageTypes)
           .map(v => parseInt(v, 10))
           .filter(v => !isNaN(v))
           .some(v => data["type"] === v));


    let msg: Message =  new Message();
    msg["type"] = data["type"];
    msg.data = data.data;

    return msg;
  }
}

export function createPullSocket(address: string): zmq.Socket {
  let sock = zmq.socket("pull");
  sock.connect(address);

  return sock;
}

export function createPubSocket(address: string): zmq.Socket {
  let sock = zmq.socket("pub");
  sock.bindSync(address);

  return sock;
}

export function newConnection(connections: Array<zmq.Socket>,
                              connection: Message): void {
  assert(typeof connection.data === "string");
  connections.push(createPullSocket(connection.data));
}
