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
  public type_: MessageTypes;
  public data: any;

  public static make(data:any): Message {
    if(typeof data.type_ !== "number" ||
      typeof data.data === "undefined" ||
      !Object.keys(MessageTypes)
           .map(v => parseInt(v, 10))
           .filter(v => !isNaN(v))
           .some(v => data.type_ === v)) {
      return null;
    }

    let msg: Message =  new Message();
    msg.type_ = data.type_;
    msg.data = data.data;

    return msg;
  }
}

export class Server {
  private clients: Array<zmq.Socket>;
  private pullSocket: zmq.Socket;

  constructor(address: string) {
    this.pullSocket = this.createPullSocket(address);
  }

  public start = function(): void {
    this.pullSocket.on("message", this.manageNewMessage);
  }

  public stop = function(): void {
    this.pullSocket.removeAllListeners();
  }

  private manageNewMessage = function(msg: any): void {
    let message: Message = Message.make(JSON.parse(msg.toString()));
    if(!message) return;

    switch(message.type_) {
      case MessageTypes.Connection:
        console.log(message);
        break
      default:
        console.log("ok");
    }
  }

  private createPullSocket = function(address: string): zmq.Socket {
    let sock = zmq.socket("pull");
    sock.connect(address);

    return sock;
  }

  private createPubSocket = function(address: string): zmq.Socket {
    let sock = zmq.socket("pub");
    sock.bindSync(address);

    return sock;
  }

  private newConnection = function( connection: Message): void {
    assert(typeof connection.data === "string");
    this.clients.push(this.createPullSocket(connection.data));
  }
}


