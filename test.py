from mathematics import Polynomial

p1 = Polynomial({12: 1, 7: 1, 2: 1})
p2 = Polynomial({8: 1, 4: 1, 3: 1, 1: 1, 0: 1})
# print(p1 + p2)
# print(p1 - p2)
# print(p1 * p2)
quotient, remainder = p1 / p2
print(quotient * p2 + remainder)
print(p1)

# print(remainder)
# print(p1 / p2)

p3 = Polynomial({5: 1, 2: 1, 1: 1})
p4 = Polynomial({3: 1, 2: 1, 0: 1})
# print(p3 ^ p4)

print(p1.additive_identity())
print(p1.additive_inverse())
print(p1 + p1.additive_inverse())
