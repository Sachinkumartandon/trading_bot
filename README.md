# Binance Futures Testnet Trading Bot

A Python-based CLI application to place **Market** and **Limit** orders on the Binance Futures Testnet (USDT-M).

## Features

- Place **Market** and **Limit** orders on Binance Futures Testnet
- Supports **BUY** and **SELL** sides
- Automatic server time synchronization (prevents signature errors)
- Input validation for order parameters
- Logging to both terminal and `bot.log` file

## Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance Futures API client
│   └── validators.py      # Input validation logic
├── cli.py                 # CLI entry point
├── bot.log                # Log file (auto-generated)
├── requirements.txt       # Dependencies
└── README.md
```

## Setup

1. **Clone the repository** (or extract the zip folder).

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API keys**:
   - Generate API keys from the [Binance Futures Testnet](https://testnet.binancefuture.com/)
   - Update your keys in `bot/client.py`

## Usage

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 50000
```

### CLI Arguments

| Argument     | Required | Description                          |
|-------------|----------|--------------------------------------|
| `--symbol`  | Yes      | Trading pair (e.g., `BTCUSDT`)       |
| `--side`    | Yes      | Order side: `BUY` or `SELL`          |
| `--type`    | Yes      | Order type: `MARKET` or `LIMIT`      |
| `--quantity`| Yes      | Quantity to trade (e.g., `0.01`)     |
| `--price`   | No       | Price for `LIMIT` orders only        |

## Example Output

```
--- Order Request Summary ---
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Qty: 0.01
Price: N/A
-----------------------------

✅ Order Placed Successfully!
Order ID: 123456789
Status: FILLED
```

## Tech Stack

- **Language**: Python 3
- **Library**: [python-binance](https://python-binance.readthedocs.io/) v1.0.19
- **API**: Binance Futures Testnet (`https://testnet.binancefuture.com`)