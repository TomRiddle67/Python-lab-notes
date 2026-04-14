driver_name = input('Hello!, what is your name: ')
age = int(input('What is your age: '))


def check_driver_age(driver_name, age):
    if age < 18:
        return f'Hello {driver_name} you are to young to drive!'
    elif age > 18:
        return f'Hello {driver_name} powering on,Enjoy the ride!'
    else:
        return f'Hello {driver_name} congratulations on your first year of driving!'
result = check_driver_age(driver_name, age)
print(result)

