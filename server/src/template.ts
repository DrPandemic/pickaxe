module Template {
  export interface Coinbaseaux {
    flag: string;
  }

  export interface Transaction {
    data: string;
    hash: string;
    depends: number[];
    fee: number;
    sigops: number;
  }

  export interface Template {
    capabilities: string[];
    version: number;
    previousblockhash: string;
    transactions: Transaction[];
    coinbaseaux: Coinbaseaux;
    coinbasevalue: number;
    longpollid: string;
    target: string;
    mintime: number;
    mutable: string[];
    noncerange: string;
    sigoplimit: number;
    sizelimit: number;
    curtime: number;
    bits: string;
    height: number;
  }
}
