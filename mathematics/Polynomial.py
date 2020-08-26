class Polynomial:
    def __init__(self, coefficients: dict):
        self.coefficients = coefficients

    def __repr__(self):
        representation = 'Polynomial{'
        for degree, coefficient in self.coefficients.items():
            representation += str(coefficient if coefficient != 1 else '') + 'x^' + str(degree) + ' '
        return representation + '}'

    def __add__(self, other):
        result = {}
        self.update_coefficients(other, result)
        self.update_coefficients(self, result)
        result = Polynomial(result)
        result.prune()
        return result

    def __sub__(self, other):
        result = {}
        self.update_coefficients(self, result)
        self.update_coefficients(other, result, factor=-1)
        result = Polynomial(result)
        result.prune()
        return result

    def __mul__(self, other):
        result = {}
        for degree1, coefficient1 in self.coefficients.items():
            for degree2, coefficient2 in other.coefficients.items():
                result[degree1 + degree2] = result.get(degree1 + degree2, 0) + coefficient1 * coefficient2
        result = Polynomial(result)
        result.prune()
        return result

    def __truediv__(self, divisor):
        dividend = Polynomial(self.coefficients.copy())
        quotient = {}
        while dividend.degree() >= divisor.degree():
            quotient_pow = dividend.degree() - divisor.degree()
            quotient_coefficient = dividend.coefficients[dividend.degree()] / divisor.coefficients[divisor.degree()]
            quotient[quotient_pow] = quotient.get(quotient_pow, 0) + quotient_coefficient
            dividend = dividend - (divisor * Polynomial({quotient_pow: quotient_coefficient}))
        return Polynomial(quotient), dividend

    def __mod__(self, divisor):
        return (self / divisor)[1]

    def __xor__(self, other):
        result = {}
        for degree, coefficient in self.coefficients.items():
            result[degree] = int(coefficient) ^ int(other.coefficients.get(degree, 0))
        for degree, coefficient in other.coefficients.items():
            result[degree] = int(coefficient) ^ int(self.coefficients.get(degree, 0))
        result = Polynomial(result)
        result.prune()
        return result

    def __neg__(self):
        result = Polynomial(self.coefficients.copy())
        for degree, coefficient in result.coefficients.items():
            result.coefficients[degree] = -coefficient
        return result

    def degree(self) -> int:
        if len(self.coefficients) == 0:
            return 0
        return max(degree for degree in self.coefficients)

    def prune(self):
        zero_coefficient_degrees = set()
        for degree, coefficient in self.coefficients.items():
            if coefficient == 0:
                zero_coefficient_degrees.add(degree)
        for degree in zero_coefficient_degrees:
            del self.coefficients[degree]

    def additive_inverse(self):
        return -self

    def to_binary(self, block_size) -> str:
        result = [0] * block_size
        for degree, coefficient in self.coefficients.items():
            result[degree] = coefficient
        return ''.join(map(str, result[::-1]))

    @staticmethod
    def update_coefficients(polynomial, coefficients, factor=1):
        for degree, coefficient in polynomial.coefficients.items():
            coefficients[degree] = coefficients.get(degree, 0) + factor * coefficient

    @staticmethod
    def additive_identity():
        return Polynomial({})

    @staticmethod
    def fromBinary(binary: str):
        result = {}
        for index, value in enumerate(binary):
            degree = len(binary) - index - 1
            if value == '1':
                result[degree] = 1
        return Polynomial(result)
