
# Tuples

my_tuple = (1, 2, 3, 5)

print(my_tuple)
print(my_tuple[0])
print(my_tuple[2])
print(my_tuple[-1])

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

conc_tuple = tuple1 + tuple2
print(conc_tuple)

rep_tuple = tuple1 * 2
print(rep_tuple)

# sets
'''
my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)
'''

# Union

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set)

# intersection

inter_set = set1.intersection(set2)
print(inter_set)              # common elements in sets

#difference

diff_set = set1.difference(set2)
print(diff_set)
