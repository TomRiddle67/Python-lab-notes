def payment_risk_processor(**transactions: dict[str | float| int]) -> dict[str, object]:
    """
     Processes a transaction and determines risk level and routing.

    Why this exists:
    Simulates a backend fraud detection pipeline that evaluates
    transactions and routes them appropriately.
    
    """
    if not transactions:
        return{
            'error': 'transactions not found'
        }

    amount = float (transactions.get('amount', 0.0))
    payment_method = transactions.get('payment_method', 'Unkown')
    country = transactions.get('country', 'Unkown')
    card_age_days = int(transactions.get('card_age_days', 0.0))

    #Risk calculation
    risk_score = 0.0
    if card_age_days < 5:
        risk_score += 0.5
    if amount > 300:
        risk_score += 0.3
    if country != 'US' and payment_method == 'card':
        risk_score += 0.2
        
    # Decision Flow
    if card_age_days < 5 and amount > 300:
        status = 'rejected'
        route = 'block'
        reason = 'High risk: new card with large transaction'
    elif amount >= 500 or risk_score > 0.5:
        status = 'review'
        route = 'manual_review'
        reason = 'Suspicious transaction requires review'
    else:
        status = 'approved'
        route = 'db_commit'
        reason = 'Transaction is safe'
    processed_amount = amount * 1.0

    return {
        'status': status,
        'risk_score': risk_score,
        'reason': reason,
        'processed_amount': processed_amount,
        'route': route,
        'payload_ready_for_db': {
            'user_id': transactions.get('user_id'),
            'amount': processed_amount,
            'status': status
        }
    }


result = payment_risk_processor(
    user_id= "U1029",
    amount= 490,
    currency= "USD",
    payment_method = "card",
    country= "NG",
    card_age_days = 10)


#E -commerce
def inventory(**order) -> dict [str,str] | dict[str]:
    """

    """
    if not order:
        return {'error': 'No orders'}
    
    items = order.get('items', [])
    priority = order.get('priority', 'standard')

    items_fullfiled: list[dict] = []
    items_backorderd: list [dict] = []

#core logic
    for item in items:
        if item ['stock'] >= item ['qty']:
            items_fullfiled.append(item)
        else:
            items_backorderd.append(item)

#logic path
    if items and len(items_backorderd) == 0:
        status = 'fullfiled'
        warehouse_route = 'nearest'
    elif items_fullfiled and items_backorderd:
        status = 'partial'
        warehouse_route = 'split'
    else: 
        status = 'delayed'
        warehouse_route = 'backorder'
    shipping_method = 'express' if priority == 'express' else 'standard'
   



    return {
    "status": status,
    "items_fulfilled": items_fullfiled,
    "items_backordered": items_backorderd,
    "shipping_method": shipping_method,
    "warehouse_route": warehouse_route,
    "api_response_ready": {
        'order_id': order.get('order_id'),
        'customer_loaction': order.get('customer_location'),
        'status': status
    }
}
    
result = inventory(
    order_id ="ORD8891",
    items = [
        {"sku": "SHOE123", "qty": 2, "stock": 10},
        {"sku": "TSHIRT99", "qty": 1, "stock": 0}
    ],
    customer_location = "Lagos",
    priority = "express"
)

print(result)