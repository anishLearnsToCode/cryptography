from mathematics import *


a = 2
p = 11

# eve
X_1 = 6
Y_1 = 9

# bob
Y_2 = 3
X_2 = discrete_log(3, 2, 11)

K = a ** (X_1 * X_2) % 11
print(K)

