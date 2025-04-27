import asyncio
from solana.transaction import Transaction,TransactionInstruction,AccountMeta
from solana.publickey import PublicKey
from solana.rpc.async_api import AsyncClient
from solana.keypair import Keypair
class OrcaClient:
    def __init__(self,rpc_url):
        self.client = AsyncClient(rpc_url)
    def keypair_from_base58(secret_b58: str) -> Keypair:
      try:
          decoded_secret = base58.b58decode(secret_b58)
          if len(decoded_secret)!=64:
              raise ValueError("expected 64 bit key here")
          return Keypair.from_secret_key(decoded_secret)
      except Exception as e:
          print(f"error decodeing the secret key:{e}")
          raise e
    async def send_transaction(self,payer:Keypair,tx:Transaction):
      try :
        tx_resp = await self.client.send_transaction(tx,payer,opts=TxOpts(skip_confirmation=False))
        return tx_resp["result"]
      except Exception as e:
        print(f'an error occured:{e}')
    async def parse_response(self, tx_sig: str):
        resp = await self.client.get_confirmed_transaction(tx_sig)
        return resp.value
    async def get_balance(self, public_key: PublicKey):
        resp = await self.client.get_balance(public_key)
        try:
            balance = resp.value
            return balance
        except Exception as e:
            print(f'{e}')
    async def close(self):
        await self.client.close()
    async def build_instruction(self,payer_pubkey: str,pool_pubkey: str,pool_authority_pubkey: str,pool_source_pubkey: str,pool_destination_pubkey: str,user_source_pubkey: str,user_destination_pubkey: str,token_program_id: str,amount_in: int,minimum_amount_out: int,program_id: str)-> Transaction:
        keys = [AccountMeta(pubkey=Pubkey.from_string(pool_pubkey),is_signer=False, is_writable=False),AccountMeta(pubkey=Pubkey.from_string(pool_authority_pubkey), is_signer=False, is_writable=False),AccountMeta(pubkey=Pubkey.from_string(user_source_pubkey),is_signer=False,is_writable=True),AccountMeta(pubkey=Pubkey.from_string(pool_source_pubkey), is_signer=False, is_writable=True),AccountMeta(pubkey=Pubkey.from_string(pool_destination_pubkey), is_signer=False, is_writable=True),
AccountMeta(pubkey=Pubkey.from_string(user_destination_pubkey),is_signer=False, is_writable=True),
AccountMeta(pubkey=Pubkey.from_string(token_program_id),is_signer=False, is_writable=False),
AccountMeta(pubkey=Pubkey.from_string(payer_pubkey),is_signer=True, is_writable=False)]
        data=amount_in.to_bytes(8,"little")+minimum_amount_out.to_bytes(8,"little")
        instruction= TransactionInstruction(keys=keys,program_id=Pubkey.from_string(program_id),data=data)
        tx=Transaction()
        tx.add(instruction)
        return tx
