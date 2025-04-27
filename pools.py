class OrcaPool:
    def __init__(self, connection, pool_info):
        self.connection = connection
        self.pool_info = pool_info
    
    def get_quote(self,input_token:str,input_amount: float):
    #Here we must implement concentrated liquidity method to get quote(orca uses whirlpool methods), 
    
    def swap(self,wallet,input_token: str,input_amount: float):
