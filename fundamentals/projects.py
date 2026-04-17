def payment_risk_processor(**transactions: dict[str | float| int]):
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
print(result)
    