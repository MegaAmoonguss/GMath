import math


def lcm(a, b):
    """
    Return the lowest common multiple of two integers.
    
    Example:
    lcm(21, 6)    # 42
    """
    assert isinstance(a, int) and isinstance(b, int), "Non-integer parameter."
    return int(abs(a * b) / math.gcd(a, b))


def factor(n):
    """
    Return all positive factors of n as a list.
    
    Example:
    factor(24)    # [1, 2, 3, 4, 6, 8, 12, 24]
    """
    if n == 0:
        return 0
    if n < 0:
        n *= -1
    
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n / i:
                factors.append(int(n / i))
    return sorted(factors)


def prime_factor(n):
    """
    Return the prime factorization of n as a list.
    
    Example:
    prime_factor(12)    # [2, 2, 3] (meaning 2 * 2 * 3)
    """
    i = 2
    factors = []
    
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
            
    if n > 1:
        factors.append(n)
    return factors


def simplify_radical(n):
    """
    Return the simplified version of sqrt(n) as a list.
    
    Example:
    simplify_radical(48)    # [4, 3] (meaning 4 * sqrt(3))
    """
    radical = [1, n]
    pfactors = prime_factor(n)
    
    i = 1
    while i < len(pfactors):
        if pfactors[i] == pfactors[i-1]:
            radical[0] *= pfactors[i]
            radical[1] //= (pfactors[i]**2)
            del pfactors[i]
        i += 1
    return radical
