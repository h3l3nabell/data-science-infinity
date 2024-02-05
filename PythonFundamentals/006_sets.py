# sets

mySet = {1, 2, 3}

mySet = set([1, 2, 3])

# sets cannot have duplicate values
mySet = {1, 1, 2, 3, 3}
print(mySet)
# removes duplicates
# cannot access by index, unordered

mySet.add(5)
mySet.update({7, 3, 9, 4, 0})
# remove an element by value - doesn't care if it exists or not
mySet.discard(11)

# throws an error if it doesn't exist
mySet.remove(11)

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

set3 = set1.difference(set2)
set4 = set2.difference(set1)

set1.difference_update(set2)


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

set3 = set1.intersection(set2)
