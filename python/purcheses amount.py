from datetime import datetime

t = datetime.now()

print ("\n")
pamount = float(input("enter purchase amount: "))

tax = pamount * 0.06

print ("\n")
print ("sales tax: " ,int(tax * 100) / 100)
print ("\n")
print ("payments: " ,(pamount + int(tax * 100) / 100))
print ("\n")
print (t)
print ("\n")