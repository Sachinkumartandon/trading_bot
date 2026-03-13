import logging
import time
from binance.client import Client
from binance.exceptions import BinanceAPIException

logger = logging.getLogger("TradingBot")

class BinanceFuturesClient:
    def __init__(self, api_key=None, api_secret=None):
        # DIRECTLY UPDATED WITH YOUR NEW KEYS
        final_api = "7ILHIIJJjoUzQQU2GWjgGYmU3Gs2UKiasCF8UWf4BpJetfKn0fWg1GGG7nRVxbEY"
        final_secret = "Vgwt0X044TBZIbvf7MHFjIJcK4L1Tw4fGWtAm72X45CCJoVmPZwgDJBPj6Pp3cG9"
        
        self.client = Client(final_api, final_secret, testnet=True)
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi/v1'
        
        # This line fixes the -1022 error by syncing with Binance time
        try:
            server_time = self.client.get_server_time()['serverTime']
            self.client.timestamp_offset = server_time - int(time.time() * 1000)
        except Exception as e:
            logger.error(f"Failed to sync time: {e}")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                'symbol': symbol.upper(),
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': quantity,
                'recvWindow': 60000 
            }
            if order_type.upper() == 'LIMIT':
                params['price'] = str(price)
                params['timeInForce'] = 'GTC'

            logger.info(f"Sending order request: {params}")
            response = self.client.futures_create_order(**params)
            return response
        except BinanceAPIException as e:
            logger.error(f"API Error: {e.status_code} - {e.message}")
            raise