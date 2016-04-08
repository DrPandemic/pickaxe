/// <reference path="typings/zmq.d.ts"/>
/// <reference path="../typings/node/node.d.ts"/>

const assert = require('assert');
const crypto = require('crypto');
import * as zmq from "zmq";
import {connectToBC} from "./bitcoin_helper";
import {BlockTemplate, Template} from "./template";

export class Server {
  private clients: Array<zmq.Socket>;
  private pullSocket: zmq.Socket;
  private pubSocket: zmq.Socket;
  private BCClient: any;
  private previousTemplate: any = null;
  private finished: boolean = false;

  constructor(host: string, port: number) {
    this.pubSocket = this.createPubSocket(host + port);
    this.BCClient = connectToBC();
    this.pullSocket = this.createPullSocket(host + (port + 1));
  }

  public start(): Promise<any> {
    console.log("Running like there is no tomorrow");

    this.pullSocket.on("message", (block: Buffer) => {
      console.log("Received a block", block.toString());

      if(this.finished)
        return;

      this.submitBlock(block.toString());
    });

    return this.run();
  }

  public stop(): void {
    this.pullSocket.removeAllListeners();
    this.finished = true;
  }

  private run(): Promise<any> {
    if(this.finished) throw new Error("Finished!");

    return this.getBlockTemplate()
      .then((template: Template) => {
        template = this.updateTemplate(template);
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

  private createPullSocket(address: string): zmq.Socket {
    let sock = zmq.socket("pull");
    sock.bindSync(address);

    return sock;
  }

  private createPubSocket(address: string): zmq.Socket {
    let sock = zmq.socket("pub");
    sock.bindSync(address);

    return sock;
  }

  private updateTemplate(template: Template): Template {
    template.hash = crypto.createHash("sha256")
      .update(JSON.stringify(template))
      .digest("hex");

    const cb0 = "03";                                       // push
    const cb1 = this.toLittleEndianNumber(template.height); // height
    const cb2 = "0".repeat(80);                             // extra nonce
    const cb3 = "2f503253482f";                             // vote
    template.coinbase = cb0 + cb1 + cb2 + cb3;              // coinbase

    return template;
  }

  // http://stackoverflow.com/a/7946195/1779927
  private toLittleEndianNumber(height: number): string {
    let hex = height.toString(16);          // translate to hexadecimal notation
    hex = hex.replace(/^(.(..)*)$/, "0$1"); // add a leading zero if needed
    let groups = hex.match(/../g);          // split number in groups of two
    groups.reverse();                       // reverse the groups
    return groups.join("");                 // join the groups back together
  }

  private broadcastTemplate(template: Template): void {
     this.pubSocket.send(JSON.stringify(template));
  }

  public submitBlock(block: string): Promise<void> {
    return this.BCClient.submitBlock(block)
      .then((msg: any) => {
        if(msg)
          console.log(msg);
        else
          console.log("The block was submitted");
      })
      .catch((error: any) => {
        console.error(error);
      });
  }
}
