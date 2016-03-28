declare module "bitcoin-core" {
  namespace BitcoinCore {
    interface ClientStatic {
      new(params?: {
        agentOptions?:any,
        headers?:boolean,
        host?:string,
        network?:string,
        password?:string,
        port?:string,
        ssl?:boolean,
        timeout?:number,
        username?:string,
        version?:string
      }): Client;
    }

    interface Client {
      getWork():any;
      getBlockTemplate():any;
    }
  }

  let bitcoinCore : BitcoinCore.ClientStatic;
  export = bitcoinCore;
}
