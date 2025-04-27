import asyncio
from client import *
from solana.publickey import PublicKey
async def main():
    orc =  OrcaClient("https://api.devnet.solana.com")
    # print('reachead here')
    # try:
    #     key = PublicKey("")
    #     balance = await orc.get_balance(key)
    #     print(f'Balance: {balance} SOL')
    # except Exception as e:
    #     print(f'Something went wrong:{e}')

        secret_b58 = ""
    # payer=OrcaClient.keypair_from_base58(secret_b58)
    # payer_pubkey=payer.public_key()
    # pool_pubkey=""
    # poolAuthorityPublicKey = ""
    # poolSourcePubkey = ""
    # poolDestinationPubkey = ""
    # userSourcePubkey = ""
    # userDestinationPubkey = ""
    # tokenProgramId = ""
    # programId = ""
    # tx = await orca_client.build_instruction()

    await orc.close()

asyncio.run(main())
  