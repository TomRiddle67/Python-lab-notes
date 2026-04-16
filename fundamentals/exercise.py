global_multiplier = 2

def calculator(a:int, b:float, name: str) -> dict[str, float | str]:
    """
    Performs arithmetic operations, scales numeric results,
    and generates a personalized summary.

    Why this exists:
    Combines computation with a user-friendly summary while keeping
    logic clean and reusable.

    Args:
        a (int): First number
        b (float): Second number
        name (str): User's name

    Returns:
        dict[str, float | str]: Scaled results and a formatted summary

    """
    sum_val = a + b
    difference_val = a - b
    product_val = a * b
    division_val = a / b
    

    calculate_output = {
        'sum': sum_val,
        'difference': difference_val,
        'product': product_val,
        'division': division_val
    }

    scaled_output = {
        key: value * global_multiplier 
        for key, value in calculate_output.items()
    }
    capitalized_name = name.capitalize()
    first_letter = name[0]
    name_length = len(name)

    summary = (f"hello {capitalized_name}! {first_letter}"
              f"Your name has {name_length} letters."
              f"sum is {scaled_output['sum']}, product is {scaled_output['product']}")

    scaled_output['summary'] = summary

    return scaled_output

result = calculator(20, 2.0, 'Tom Riddle')
print(result)
