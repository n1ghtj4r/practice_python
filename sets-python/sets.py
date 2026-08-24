my_set = {1, 2, 3, 4, 5} 

#set() # Set
#{}    # Dictionary

my_set.add(6)
#{1, 2, 3, 4, 5, 6}

my_set.add(5)
#{1, 2, 3, 4, 5, 6} //will not change any

my_set.remove(4)
my_set.discard(4)

my_set.clear() #The .clear() method removes all the elements from the set

print(f"sets: \"{bool(my_set)}\", false means empty/null and true means it has value")

my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set)) # False
print(my_set.issuperset(your_set)) # False
print(my_set.isdisjoint(your_set)) # False

print(my_set | your_set) # {1, 2, 3, 4, 5, 6}
print(my_set & your_set) # {2, 3, 4}
print(my_set - your_set) # {1, 5}
print(my_set ^ your_set) # {1, 5, 6}

#|= &= -= ^=

my_set -= your_set

print(my_set) # {1, 5}

print(5 in my_set) #condition, output true