# The function for finding a key in the list 
def linearSearch(lst, key):
    for i in range(0, len(lst)): 
        if key == lst[i]:
            return i

    return -1

linearSearch([9,3,6,1,4],  3)  # Output: 1