from eth_utils import (
    decode_hex,
)

# This block is a child of the genesis defined in the chain fixture above and contains
# a single tx that transfers 10 wei from 0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b to
# 0x095e7baea6a6c7c4c2dfeb977efac326af552d87.
valid_block_rlp = decode_hex(
    "0x"
    "f90260f901f9a07285abd5b24742f184ad676e31f6054663b3529bc35ea2fcad"
    "8a3e0f642a46f7a01dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413"
    "f0a142fd40d49347948888f1f195afa192cfee860698584c030f4c9db1a0964e"
    "6c9995e7e3757e934391b4f16b50c20409ee4eb9abd4c4617cb805449b9aa053"
    "d5b71a8fbb9590de82d69dfa4ac31923b0c8afce0d30d0d8d1e931f25030dca0"
    "bc37d79753ad738a6dac4921e57392f145d8887476de3f783dfa7edae9283e52"
    "b901000000000000000000000000000000000000000000000000000000000000"
    "0000000000000000000000000000000000000000000000000000000000000000"
    "0000000000000000000000000000000000000000000000000000000000000000"
    "0000000000000000000000000000000000000000000000000000000000000000"
    "0000000000000000000000000000000000000000000000000000000000000000"
    "0000000000000000000000000000000000000000000000000000000000000000"
    "0000000000000000000000000000000000000000000000000000000000000000"
    "0000000000000000000000000000000000000000000000000000000000000000"
    "0000008302000001832fefd8825208845754132380a0194605bacef646779359"
    "318c7b5899559a5bf4074bbe2cfb7e1b83b1504182dd88e0205813b22e5a9cf8"
    "61f85f800a82c35094095e7baea6a6c7c4c2dfeb977efac326af552d870a801b"
    "a0f3266921c93d600c43f6fa4724b7abae079b35b9e95df592f95f9f3445e94c"
    "88a012f977552ebdb7a492cf35f3106df16ccb4576ebad4113056ee1f52cbe49"
    "78c1c0"
)
