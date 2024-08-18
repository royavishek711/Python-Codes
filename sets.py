# user_set={} # it will create an empty dictionary
# user_set=set() # it will create an empty set
# print(type(user_set))


user_set={1,2,3,4,5}
new_set={10,2,12,1,19,5}
other_set={2,30,40}
# user_set.add(69)
# user_set.remove(4)
#discard(item): Removes a specific element from the set. If the element is not found, it does nothing (no error is raised).
# user_set.discard(100)
# user_set.discard(100)
#union(*others): Returns a new set with all elements from the set and all others (can be other sets or iterables).
print(user_set.union(new_set))
#intersection(*others): Returns a new set with elements that are common to the set and all others.
print(user_set.intersection(new_set))
#difference(*others): Returns a new set with elements in the set that are not in the others.
print(user_set.difference(new_set))
print(new_set.difference(user_set))
#symmetric_difference(other): Returns a new set with elements in either the set or the other, but not in both.
print(new_set.symmetric_difference(user_set))
#issubset(other): Returns True if the set is a subset of the other set.
print(other_set.issubset(user_set))
#issuperset(other): Returns True if the set is a superset of the other set.
print(user_set.issuperset(other_set))
#isdisjoint(other): Returns True if the set has no elements in common with the other set.
print(user_set.isdisjoint(other_set))