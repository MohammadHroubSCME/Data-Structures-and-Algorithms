t1 = () # Create an empty tuple

t2 = (1, 3, 5) # Create a set with three elements

# Create a tuple from a list
t3 = tuple([2 * x for x in range(1, 5)]) 

# Create a tuple from a string
t4 = tuple("abac") # t4 is ['a', 'b', 'a', 'c'] 

t5 = t1+t2+t3+t4
print (t5)