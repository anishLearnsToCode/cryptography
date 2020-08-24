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

