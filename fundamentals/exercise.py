def calculator(a:int, b:float):
    calculate_input = {
        'sum': a + b,
        'difference': a-b,
        'product': a * b,
        'division': a / b
    }
    return calculate_input
result = calculator(10, 7.1)
print(result)