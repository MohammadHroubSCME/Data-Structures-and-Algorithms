def printgrade(score):

    if score >= 90.0:
        print ('A')
    elif score >= 80.0:
        print ('B')
    elif score >= 70.0:
        print ('C')
    elif score >= 60.0:
        print ('D')
    else:
        print ('F')

def main():
    score = float(input("Enter the score: "))
    print ("The grade is: " ,end = "")
    printgrade(score)

main()