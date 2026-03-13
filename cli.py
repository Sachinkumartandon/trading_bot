import argparse
import logging
import sys
import os

# Fix Windows terminal encoding for emoji/unicode
if os.name == 'nt':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
from bot.client import BinanceFuturesClient

# Configure logging to show output in terminal and save to bot.log
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

def main():
    parser = argparse.ArgumentParser(description='Binance Futures CLI Trading Bot')
    parser.add_argument('--symbol', type=str, required=True, help='Trading symbol (e.g., BTCUSDT)')
    parser.add_argument('--side', type=str, required=True, choices=['BUY', 'SELL'], help='Order side')
    parser.add_argument('--type', type=str, required=True, choices=['MARKET', 'LIMIT'], help='Order type')
    parser.add_argument('--quantity', type=float, required=True, help='Quantity to trade')
    parser.add_argument('--price', type=float, help='Price for LIMIT orders')

    args = parser.parse_args()

    # --- UPDATED SECTION ---
    # We no longer check for os.getenv here because the keys 
    # are already hard-coded inside BinanceFuturesClient in client.py
    try:
        client = BinanceFuturesClient()
        
        print(f"\n--- Order Request Summary ---")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Qty: {args.quantity}")
        print(f"Price: {args.price if args.price else 'N/A'}")
        print(f"-----------------------------\n")

        # Place the order
        response = client.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print(f"✅ Order Placed Successfully!")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")

    except Exception as e:
        print(f"\n❌ Order Failed: {e}")

if __name__ == "__main__":
    main()