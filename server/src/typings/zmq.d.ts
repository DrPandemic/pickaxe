/// <reference path="../../typings/node/node.d.ts"/>

declare module "zmq" {
  import {EventEmitter} from 'events';

  export type types =
    "pub"
  | "xpub"
  | "sub"
  | "xsub"
  | "req"
  | "xreq"
  | "rep"
  | "xrep"
  | "push"
  | "pull"
  | "dealer"
  | "router"
  | "pair"
  | "stream";

  export interface Socket extends EventEmitter {
    bindSync(address: string): Socket;

    send(data: any, flag?: number): void;

    connect(address: string, callback?: Function): Socket;

    close(): Socket;

    subscribe(channel: string): void;
  }

  export function socket(type_: types): Socket;
}
