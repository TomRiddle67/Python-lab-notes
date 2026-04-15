users = [
    {"username": "tom", "password": "1234", "is_active": True},
    {"username": "john", "password": "abcd", "is_active": False},
]

def login(username, password):
    for user in users:
        if user['username']== username:
            if user['password'] != password:
                return 'Incorrect Password'
            if not user['is_active']:
                return 'Account Disabled'
            return 'login succesful'
    return 'User not found'
user_login = login('tim', '1234')
print(user_login)
        


