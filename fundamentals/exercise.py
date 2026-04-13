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

# cart = [{
#     'name': 'shoes',
#     'price': 80,
#     'quantity': 1
# },
# {   'name': 'jacket',
#     'price': 50,
#     'quantity': 2
# }]

# total = 0

# for item in cart:
#     total+= item['price'] * item['quantity']
# if total > 100:
#     print ('You have a discount')
# else:
#     print('cart not full')

#----------------
#friend access system
#-----------------

# user = {
#     'name': 'Tom',
#     'is_friend': False,
#     'is_blocked': False
# }

# if user.get('is_blocked'):
#     print('Access denied')

# elif user.get('is_friend'):
#     print('message allowed')
# else:
#     print('send a friend request') #👨‍🦯👨‍🦯 not bad


#cleaner version...
user = {
    'name': 'Tom',
    'is_friend': False,
    'is_blocked': True
}

is_blocked = user.get('is_blocked')
is_friend = user.get('is_friend')

if is_blocked:
    print ('Access Denied!')
elif is_friend:
    print ('Message Allowed')
else:
    print('send a friend request')
