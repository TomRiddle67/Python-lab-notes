# user_age = 40
# user_name = "Tom"

# man, is_from, works_at = "Tom", "London", "KFC"

# # print(user_name, user_age)
# print(man, is_from, works_at)

# #statements and expressions
# kids_age = (user_age // 2)
# print (kids_age)

username = input("username: ")
password = input("password: ")
user_password = password.replace( password[2], "****")

print(f"welcome {username} your password is {user_password} ")