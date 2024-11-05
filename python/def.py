#def sum (i1 ,i2):
#    result = 0
#    for i in range (i1 ,i2 + 1):
#        result += i
#    return result
#
#def main():
#    print ("Sum from  1 to 10 is:", sum (1 ,10))
#    print  ("Sum from  20 to 37 is:", sum (20 ,37))
#    print   ("Sum from  35 to 49 is:", sum (35 ,49))
#
#main()

def sum(i1, i2):
    result = 0
    for i in range(i1, i2 + 1):
        result += i
    return result

def main():
    # Prompting the user for input
    i1 = int(input("Enter the first value: "))
    i2 = int(input("Enter the second value: "))
    
    # Calculating and displaying the result
    print("The sum from", i1, "to", i2, "is:", sum(i1, i2))

main()