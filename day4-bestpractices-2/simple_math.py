"""
A collection of simple math operations
"""

def simple_add(a,b):
    return a+b
    """
    add(a, b)

    The sum of two numbers.

    """

def simple_sub(a,b):
    return a-b

    """
    sub(a, b)

    The subtaction of two numbers.

    """

def simple_mult(a,b):
    return a*b
    
    """
    mult(a, b)

    The multiplication of two numbers.
    
    Parameters
    ----------
    a: number
    b: number
    
    Returns
    -------
    Product of multiplication
    """

def simple_div(a,b):
    return a/b

def poly_first(x, a0, a1):
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
