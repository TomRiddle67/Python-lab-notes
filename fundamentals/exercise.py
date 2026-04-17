global_multiplier = 2
def calculator(a:int, b: float, name: str) -> dict[str, float | str | list[str]]:
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
    diff_val = a - b
    product_val = a * b
    division_val = a / b

    base_results = {
        'sum': sum_val,
        'difference': diff_val,
        'product': product_val,
        'division': division_val
    }

    scaled_results = {
        key: value * global_multiplier
        for key, value in base_results.items()
    }

    capitalized_name = name.capitalize()
    first_letter = name[0]
    name_length = len(name)

    summary = (f"hello {capitalized_name}! {first_letter} " 
              f"Your name has {name_length} letters."
              f" sum is {scaled_results['sum']}, product is {scaled_results['product']}")

    history = [
        f"{key}: {value}"
        for key, value in scaled_results.items()
    ]

    indexed_history = [
        f"[{index + 1:02}] {value}"
        for index, value in enumerate(history)
    ] 

    status = 'High' if scaled_results['sum'] > 50 else 'Low'

    
    scaled_results['summary'] = summary
    scaled_results['history'] = history
    scaled_results['status'] = status
    scaled_results['indexed_history'] = indexed_history


    return scaled_results

result = calculator(7, 1.1, 'tom Riddle')
print(result)