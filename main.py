import asyncio
from client import *
from solana.publickey import PublicKey
async def main():
    orc =  OrcaClient("https://api.devnet.solana.com")
    print('reachead here')
    try:
        key = PublicKey("")
        balance = await orc.get_balance(key)
        print(f'Balance: {balance} SOL')
    except Exception as e:
        print(f'Something went wrong:{e}')
    await orc.close()


asyncio.run(main())
  
