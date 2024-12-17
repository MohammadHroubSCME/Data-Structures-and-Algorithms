from lnklst import Lnkst

lst = LinkedList()
lst.add('b') 
lst.add('i') 
lst.add('t') 
lst.add('c')
lst.add('o')
lst.add('i')
lst.add('n')
print(lst)

for e in lst:
    print(e, end = ' ')
print()

iterator = iter(lst)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))