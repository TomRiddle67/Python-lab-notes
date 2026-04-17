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


def flexible_calculator(*numbers: float) -> dict[str, float]:
    """
    Performs aggregate calculations on a flexible number of inputs.

    Why this exists:
    Allows dynamic input handling for scenarios like analytics,
    user-provided datasets, or API payloads without fixed parameters.

    Args:
        *numbers (float): Variable number of numeric inputs

    Returns:
        dict[str, float]: Summary statistics including sum, average, max, and min
    """
    if not numbers:
        return {
            'sum': 0.0,
            'average': 0.0,
            'max': 0.0,
            'min': 0.0
        }
    total = sum(numbers)
    average = total / len(numbers)

    return {
        'sum': total,
        'average': average,
        'max': max(numbers),
        'min': min(numbers)

    }
result = flexible_calculator()


def user_profile(**data: str) -> dict[str, int] :
    """
    Builds a dynamic user profile from flexible keyword inputs.

    Why this exists:
    Allows backend systems to accept and process user data dynamically,
    similar to handling JSON payloads in APIs.

    Args:
        **data (str): Arbitrary user attributes (e.g., name, role, country)

    Returns:
        dict[str, str]: User data with a generated summary

    """
    if not data:
        return{
            'error': 'User not found'
        }
    name = data.get('name', 'Unknown')
    role = data.get('role', 'Unknown')
    country = data.get('country', 'Unknown')
    fields_count = len(data)

    summary = f"{name} is a {role} from {country}"
    data['summary'] = summary
    data['fields_count'] = fields_count
    return data

result = user_profile(name ='Snow',role = 'Software engineer', country = 'Nigeria' )


def process_orders(*prices: float, discount: float = 0.0) -> dict[str, float]:
    """
    Processes a list of order prices and applies an optional discount.

    Why this exists:
    Simulates backend order processing logic where totals and discounts
    must be calculated dynamically and safely.

    Args:
        *prices (float): Variable list of item prices
        discount (float): Discount rate (e.g., 0.1 for 10%)

    Returns:
        dict[str, float | str]: Order totals and summary

    """
    if not prices:
        return{
        'total': 0.0,
        'final_total': 0.0,
        'discount_applied': 0.0

        }

    total = sum(prices)
    discount_applied = total * discount
    final_total = total - discount_applied
    summary = f" Total: {total} Final_Total: {final_total}"
    return {
        'total': total,
        'final_total': final_total,
        'discount_applied': discount_applied,
        'summary': summary
    }
result = process_orders(30.0, 12.0, 90.2, discount = 0.1)

def analyze_transcations(*transactions: float, threshold: float = 50.0) -> dict[str,float | int | str]:
    """
    Analyzes a list of transactions and returns summary statistics.

    Why this exists:
    Simulates backend financial or analytics processing where we compute
    totals, counts, and business status dynamically.

    Args:
        *transactions (float): Variable number of transaction values
        threshold (float): Value used to determine high or low status

    Returns:
        dict[str, float | int | str]: Aggregated analytics result

    """
    if not transactions:
        return {
            'total': 0.0,
            'count': 0,
            'status': 'Nil',
            'message': 'No transactions'
        }

    total = sum(transactions)
    if (count := len(transactions)) > 0:
        status = 'High' if total > threshold else 'Low'
    message = f"Total {total} | Status {status}"

    return{
        'total': total,
        'count': count,
        'status': status,
        'message': message

    }
result = analyze_transcations(35.5, 15.0, 80.0)
print(result)