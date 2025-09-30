import doctest
from sympy import randprime


def generate_keys(number_of_bits):
    halfbits = number_of_bits / 2 
    q = randprime(pow(2,halfbits -1), pow(2,halfbits))
    p = randprime(pow(2,halfbits -1), pow(2,halfbits))
    while (q == p):
        p = randprime(pow(2,halfbits -1), pow(2,halfbits))
    
    n = p * q



#stack overflow: (LINK)[https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python]
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def powcustom(base, exponent, modulo)-> int:
    """
    test the multiplicative inverse
    >>> powcustom(3,-1,7)
    5

    test big numbers
    >>> powcustom (115,223,27)
    16

    """

    #calculate the multiplicative inverse
    if exponent < 0:
        base = modinv(base, modulo)
        exponent = -exponent
    #if the exponent is set to 0  return 1 % <modulo>
    if exponent == 0:
        return 1 % modulo
    #if the expnent is 1 return 
    if exponent == 1:
        return base % modulo

    if (exponent%2 == 0):
        half = powcustom(base, exponent // 2, modulo)
        return (half * half) % modulo
    else:
        half = powcustom(base, (exponent-1) // 2, modulo)
        return (half * half * base) % modulo

doctest.testmod()
