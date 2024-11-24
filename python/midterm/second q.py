print ("*********************************************")
print ("welcome to my program (school certified)")
print ("*********************************************")

name = input("enter student name: ")
print ("welcome", name)
print ("select the specialization: ")
print ("1. Literary")
print ("2. Science\n")
spec = input("select number 1 or 2: ")
if spec == "1":
    print ("Literary: ")
    print ("NOTE: all marks are out of 100")

    x = float(input ("1. English: "))
    c = float(input ("2. Math: "))
    v = float(input ("3. History: "))
    b = float(input ("4. Geography: "))
    n = float(input ("5. Arabic: "))
    m = float(input ("6. Technology: "))
    print ("\nMarks rate= " ,(x+c+v+b+n+m)/6)
    
elif spec == "2":
    print ("Science: ")
    print ("NOTE: all marks are out of 100")

    a = float(input ("1. Biology: "))
    s = float(input ("2. Chemistry: "))
    d = float(input ("3. Physics: "))
    f = float(input ("4. Math: "))
    g = float(input ("5. Technology: "))
    h = float(input ("6. Arabic: "))
    j = float(input ("7. English: "))
    print ("\nMarks rate= " ,(a+s+d+f+g+h+j)/7)
    
