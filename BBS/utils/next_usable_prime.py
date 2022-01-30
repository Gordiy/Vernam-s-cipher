import sympy


def next_usable_prime(x):
    """Find value that equal x mod 4 = 3."""
    p = sympy.nextprime(x)
    while (p % 4 != 3):
        p = sympy.nextprime(p)
    return p
