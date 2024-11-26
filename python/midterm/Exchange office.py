import datetime
print ("**********************************")
print ("Welcome to our Exchange office")
print ("**********************************\n")
print ("enter the process you want to do: ")
print ("1. exchange JOD to ILS")
print ("2. exchange USD to ILS\n")
q = input ("select the conversation number: ")

def exchange():
    if q == "1":
        print ("you selected to exchange JOD to ILS")
        w = float(input("enter the amount of JOD you want to exchange: "))
        print (" it's equal " ,w*5.3 ,"JOD")

    elif q == "2":
        print ("you selected to exchange USD to ILS")
        e = float(input("enter the amount of USD you want to exchange:"))
        print (" it's equal " ,e*3.7 ,"ILS")
        
    else :
        Print("wrong number , please try again")

    total = float(0.0)
    
    return total
exchange()
print ("thank you for using our service")
print ("see you next time")
print ("**********************************")
now = datetime.datetime.now()
print (now)