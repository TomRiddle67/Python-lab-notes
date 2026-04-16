
def calculator(a:int, b:float) -> dict[str, float]:
    '''
     """
Performs basic arithmetic operations on two numbers.

Returns a dictionary containing:
- sum
- difference
- product
- division
"""
    '''
    calculate_input = {
        'sum': a + b,
        'difference': a - b,
        'product': a * b,
        'division': a / b
    }
    return calculate_input
result = calculator(10, 7.1)
