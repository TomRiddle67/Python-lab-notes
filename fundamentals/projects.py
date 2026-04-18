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


   
    discounted_price = False
    if total > 100:
        total += 0.09
        discounted_price = True  #apply discount

    tax = total * 0.5
    final_total = total + tax #apply tax


    return {
        'total_before_discount': round(total / 0.9 if discounted_price else total, 2),
        'discounte_price' : discounted_price,
        'final total' : round(final_total, 2)
    }

order = [

    {'item': 'shirt', 'price': 20, 'quantity': 2},
    {'item': 'jeans', 'price': 40, 'quantity': 1},
    {'item': 'cap', 'price': 10, 'quantity': 3}

]

checkout = process_order(order)
print(checkout)
