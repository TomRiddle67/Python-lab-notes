def process_order(order: list[dict]) -> dict:
    """
    
    """
    if not order:
        return {'error': 'No orders'}

    total = 0

    for item in order:
        if item['price'] < 0 and item['quantity'] < 0:
            return {'error': 'Invalid data'}
    total += item['price'] * item['quantity'] # Calculate total cost
