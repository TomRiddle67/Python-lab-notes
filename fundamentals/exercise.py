global_multiplier = 2

def calculator(a:int, b:float) -> dict[str, float]:
    """
    Performs basic arithmetic operations on two numbers.

    Returns a dictionary containing scaled results
    """

    calculate_output = {
        'sum': a + b,
        'difference': a - b,
        'product': a * b,
        'division': a / b
    }

    scaled_output = {
        key: value * global_multiplier
        for key, value in calculate_output.items()
    }
    return scaled_output
result = calculator(20, 2.0)
