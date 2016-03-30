interface Coinbaseaux {
  flag: string;
}

interface Transaction {
  data: string;
  hash: string;
  depends: number[];
  fee: number;
  sigops: number;
}

class ITemplate {
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

  [key: string]: any;
}

class Template extends ITemplate {
  constructor(obj: ITemplate) {
    super();
    for (let propName in obj) {
      this[propName] = <any>obj[propName]
    }
  }
}

export default Template;
