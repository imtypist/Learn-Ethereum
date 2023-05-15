from web3 import Web3, EthereumTesterProvider
from eth_tester import PyEVMBackend
from solcx import install_solc, compile_source
install_solc(version='latest')


w3 = Web3(EthereumTesterProvider(ethereum_tester=PyEVMBackend()))

compiled_sol = compile_source(
    '''
    pragma solidity >0.5.0;

    contract Greeter {
        string public greeting;

        constructor() public {
            greeting = 'Hello';
        }

        function setGreeting(string memory _greeting) public {
            greeting = _greeting;
        }

        function greet() view public returns (string memory) {
            return greeting;
        }
    }
    ''',
    output_values=['abi', 'bin']
)

contract_id, contract_interface = compiled_sol.popitem()
bytecode = contract_interface['bin']
print(bytecode)
abi = contract_interface['abi']
print(abi)
w3.eth.default_account = w3.eth.accounts[0]
print(w3.eth.accounts)

Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = Greeter.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(tx_receipt)

greeter = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

print(greeter.functions.greet().call())

tx_hash = greeter.functions.setGreeting('Nihao').transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(greeter.functions.greet().call())

