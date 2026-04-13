# cart = [{
#     'name': 'shoes',
#     'price': 80,
#     'quantity': 1
# },
# {   'name': 'jacket',
#     'price': 50,
#     'quantity': 2
# }
# ]
# total = 100
# cart_total = cart[1].get('price') * cart[1].get('quantity') + cart[0].get('price') * cart[0].get('quantity')
# if cart_total > total:
#     print('You have a discount')
# else:
#     print('cart not full') #my code  😂🤦‍♂️

#Cleaner version

cart = [{
    'name': 'shoes',
    'price': 80,
    'quantity': 1
},
{   'name': 'jacket',
    'price': 50,
    'quantity': 2
}]

total = 0

for item in cart:
    total+= item['price'] * item['quantity']
if total > 100:
    print ('You have a discount')
else:
    print('cart not full')