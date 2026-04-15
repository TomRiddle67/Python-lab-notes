account = {
    "name": "Tom",
    "balance": 100,
    "is_active": True
}
def bank_action(account,action,amount=0):
    if not account['is_active']:
        return 'Account is inactive'
    if action == 'balance':
        return account['balance']
    if action == 'deposit':
        account['balance'] += amount
        return amount['balance']
    if action == 'withdraw':
        if amount > account['balance']:
            return 'insufficent funds'
        account['balance'] -= amount
        return account['balance']
    return 'invalid action'
print(bank_action(account, 'withdraw', amount=80))
        
    