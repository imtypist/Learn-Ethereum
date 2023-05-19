# Learn Ethereum Protocol By Reading Code

Install the Python implementation of Ethereum protocol [py-evm](https://github.com/ethereum/py-evm) through source code, recommend to install required packages under virtualenv.

```bash
$ cd eth-tester && pip3 install -e ".[dev]"
$ cd py-evm && pip3 install -e ".[dev]"
$ pip3 install web3 py-solc-x
```

A minimal case to compile, deploy, execute smart contracts using [eth-tester](https://github.com/ethereum/eth-tester) with py-evm backend.

```bash
$ python3 main.py
```

The [guides](https://py-evm.readthedocs.io/en/latest/guides/understanding_the_mining_process.html) to build a mining chain using py-evm.

```bash
$ python3 test-pyevm.py
```

