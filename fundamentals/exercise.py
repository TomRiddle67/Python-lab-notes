order = [
    {"item": "shirt", "price": 20, "quantity": 2},
    {"item": "jeans", "price": 40, "quantity": 1}
]

def calculate_total(order, tax=0.5):
    total= 0
    for item in order:
        total+= item['price'] * item['quantity']
        
        #add tax
        total_with_tax = total + (total * tax)
    if total_with_tax > 100:

        #apply discount
        discount = total_with_tax * 0.10
        total_with_tax -= discount
    return total_with_tax
print(calculate_total(order))
