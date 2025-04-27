import asyncio
from client import *
from solana.publickey import PublicKey
async def main():
# here there is a logic to write the code for invoking the orcaClient Class
    orc =  OrcaClient("https://api.devnet.solana.com")
    # print('reachead here')
    # try:
    #     key = PublicKey("")
    #     balance = await orc.get_balance(key)
    #     print(balance)

    # except Exception as e:
    #     print('Something went wrong:{e}')
    await orc.close()


asyncio.run(main())
  