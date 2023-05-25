# https://louisabraham.github.io/articles/no-abi.html

from evmdasm import EvmBytecode
from solcx import install_solc, compile_source
install_solc(version='latest')

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
# print(bytecode)
abi = contract_interface['abi']
# print(abi)

opcodes = EvmBytecode(bytecode).disassemble()

for i in range(len(opcodes) - 3):
    # can be seen as contract function entries
    if (
        opcodes[i].name == "PUSH4"
        and opcodes[i + 1].name == "EQ"
        and opcodes[i + 2].name == "PUSH2"
        and opcodes[i + 3].name == "JUMPI"
    ):
        print(opcodes[i].operand)
        print(opcodes[i+2].operand)

for opcode in opcodes:
    try:
        print("%x: %s %s" % (opcode.address, opcode.name, opcode.operand))
    except:
        print("%x: %s" % (opcode.address, opcode.name))
