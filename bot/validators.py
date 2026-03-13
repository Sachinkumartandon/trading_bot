
def validate_inputs(symbol, side, order_type, quantity, price):
    side = side.upper()
    order_type = order_type.upper()
    
    if side not in ['BUY', 'SELL']:
        raise ValueError("Side must be BUY or SELL")
    if order_type not in ['MARKET', 'LIMIT']:
        raise ValueError("Order type must be MARKET or LIMIT")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    if order_type == 'LIMIT' and (price is None or price <= 0):
        raise ValueError("Price must be provided and > 0 for LIMIT orders")
        
    return symbol.upper(), side, order_type, quantity, price