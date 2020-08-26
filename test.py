from mathematics import PBox

expansion_p_box = PBox({1: 1, 2: 2, 3: [3, 4]})
print(expansion_p_box)
print('In Degree:', expansion_p_box.in_degree)
print('Out Degree:', expansion_p_box.out_degree)
print(expansion_p_box.permutate([10, 20, 30]))

print(expansion_p_box.is_invertible())

compression_p_box = PBox({1: 1, 2: [], 3: 2})
# print(compression_p_box.in_degree)
# print(compression_p_box.out_degree)
# print(compression_p_box.permutate([10, 20, 30]))
print(compression_p_box.is_invertible())
p_box = PBox({1: 3, 2: 1, 3: 2})
print(p_box.in_degree)
print(p_box.out_degree)
print(p_box.permutate([10, 20, 30]))

print(p_box.is_invertible())
print(p_box.invert())
print(p_box.invert().permutate(p_box.permutate([10, 20, 30])))
