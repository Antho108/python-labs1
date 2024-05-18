# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """_Transform KM to Miles_

    Args:
        km (_int_): _variable Kilometers..., 45_

    Returns:
        _int_: _ The kilometers in Miles! 22 miles!
    """

    

    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
