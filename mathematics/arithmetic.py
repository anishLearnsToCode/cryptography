import numpy as np
from numpy import linalg


def gcd(a, b):
    return gcd(b, a % b) if b != 0 else a


def extended_gcd(a, b):
    s, old_s = 1, 0
    t, old_t = 0, 1

    while b != 0:
        q = a // b
        a, b = b, a % b
        s, old_s = old_s, s - q * old_s
        t, old_t = old_t, t - q * old_t
    return a, s, t


def diophantine_sol_exists(a, b, c):
    hcf = gcd(a, b)
    return c % hcf == 0


# returns solution of diophantine equation in form (x, y) if exists
# returns the particular solution otherwise returns nothing
def diophantine(a, b, c):
    hcf = gcd(a, b)
    # solution exits
    if c % hcf == 0:
        _, s, t = extended_gcd(a / hcf, b / hcf)
        return int((c / hcf) * s), int((c / hcf) * t)


def diophantine_general(a, b, c, iters=10):
    if diophantine_sol_exists(a, b, c):
        x, y = diophantine(a, b, c)
        hcf = gcd(a, b)
        for i in range(iters):
            yield x + i * (b // hcf), y - i * (a // hcf)


def additive_inverse(a, n):
    return (n - a) % n


def multiplicative_inverse_exists(a, n):
    return gcd(a, n) == 1


def multiplicative_inverse(b, n):
    if multiplicative_inverse_exists(b, n):
        return (extended_gcd(n, b)[2] + n) % n


def sol_single_var_le(a, b, n, c=0):
    if c != 0:
        b = (b - c) % n

    hcf = gcd(a, n)
    sols = []
    if b % hcf == 0:
        a, b, n = a // hcf, b // hcf, n // hcf
        x_0 = (b * multiplicative_inverse(a, n)) % n
        for k in range(hcf):
            sols.append(x_0 + k * n)
    return sols


def modMatInv(A, p):  # Finds the inverse of matrix A mod p
    n = len(A)
    adj = np.zeros(shape=(n, n))
    for i in range(0, n):
        for j in range(0, n):
            adj[i][j] = ((-1) ** (i + j) * int(round(linalg.det(minor(A, j, i))))) % p
    return (modInv(int(round(linalg.det(A))), p) * adj) % p


def modInv(a, p):  # Finds the inverse of a mod p, if it exists
    for i in range(1, p):
        if (i * a) % p == 1:
            return i
    raise ValueError(str(a) + " has no inverse mod " + str(p))


def minor(A, i, j):  # Return matrix A with the ith row and jth column deleted
    A = np.array(A)
    sub_matrix = np.zeros(shape=(len(A) - 1, len(A) - 1))
    p = 0
    for s in range(0, len(sub_matrix)):
        if p == i:
            p = p + 1
        q = 0
        for t in range(0, len(sub_matrix)):
            if q == j:
                q = q + 1
            sub_matrix[s][t] = A[p][q]
            q = q + 1
        p = p + 1
    return sub_matrix


def is_prime(number: int) -> bool:
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def product(numbers: list) -> int:
    result = 1
    for number in numbers:
        result *= number
    return result


def relatively_prime(a: int, b: int) -> bool:
    return gcd(a, b) == 1


def exp_func(x, y):
    exp = bin(y)
    value = x

    for i in range(3, len(exp)):
        value = value * value
        if exp[i:i + 1] == '1':
            value = value * x
    return value


def mod_exponentiation(X, E, m):
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E /= 2
        else:
            Y = (X * Y) % m
            E -= 1
    return Y


def totient(number: int) -> int:
    count = 0
    for i in range(1, number):
        if gcd(number, i) == 1:
            count += 1
    return count


def relatively_prime_numbers(n):
    numbers = []
    for i in range(1, n):
        if relatively_prime(i, n):
            numbers.append(i)
    return numbers


def crt_representation(number: int, crt: tuple) -> list:
    result = []
    for mod in crt:
        result.append(number % mod)
    return result


def are_pairwise_relatively_prime(numbers) -> bool:
    for i, number in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            if not relatively_prime(number, numbers[j]):
                return False
    return True


# noinspection PyTypeChecker
def valid_crc(crc: tuple, number: int) -> bool:
    return are_pairwise_relatively_prime(crc) and product(crc) == number


def is_product_of_2_primes(number: int) -> bool:
    for i in range(2, number):
        if number % i == 0:
            quotient = number // i
            if is_prime(i) and is_prime(quotient):
                return True
    return False


def discrete_log_table(number: int) -> list:
    table = []
    for i in range(1, number):
        row = []
        for j in range(1, number):
            row.append(pow(i, j, number))
        table.append(row)
    return table


def discrete_log(n, b, m):
    for i in range(m):
        if pow(b, i, m) == n:
            return i
