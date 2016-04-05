/// <reference path="typings/zmq.d.ts"/>
/// <reference path="../typings/node/node.d.ts"/>

import * as zmq from "zmq";
const assert = require('assert');
import {connectToBC} from "./bitcoin_helper";
import {BlockTemplate, Template} from "./template";

export enum MessageTypes {
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
      console.error("Packet was malformed");
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
  private pubSocket: zmq.Socket;
  private BCClient: any;
  private previousTemplate: any = null;
  private finished: boolean = false;

  constructor(address: string) {
    this.pubSocket = this.createPubSocket(address);
    this.BCClient = connectToBC();
  }

  public start(): Promise<any> {
    return this.run();
  }

  public stop(): void {
    this.finished = true;
  }

  private run(): Promise<any> {
    console.log("Running like there is no tomorrow");

    if(this.finished) throw new Error("Finished!");

    return this.getBlockTemplate()
      .then((template: Template) => {
        console.log(template);
        this.broadcastTemplate(template);

        return this.delay();
      }).then(() => {
        return this.run();
      }).catch((error: any) => {
        console.error(error);
      });
  }

  private delay(): Promise<any> {
    return new Promise(resolve => setTimeout(resolve, 5 * 1000));
  }

  private getBlockTemplate(): Promise<Template> {
    return this.BCClient.getBlockTemplate()
    .then((results:BlockTemplate) => {
      let template:Template = new Template(results);

      return template;
    });
  }

  private manageNewMessage(msg: any): void {
    let message: Message = Message.make(JSON.parse(msg.toString()));
    if(!message) return;

    switch(message.type_) {
      default:
        console.log("ok");
        break;
    }
  }

  private createPullSocket(address: string): zmq.Socket {
    let sock = zmq.socket("pull");
    sock.connect(address);

    return sock;
  }

  private createPubSocket(address: string): zmq.Socket {
    let sock = zmq.socket("pub");
    sock.bindSync(address);

    return sock;
  }

  private broadcastTemplate(template: Template): void {
     let message: Message = new Message();

     message.type_ = MessageTypes.NewTemplate;
     message.data = template;

     this.pubSocket.send(JSON.stringify(message));
  }
}
