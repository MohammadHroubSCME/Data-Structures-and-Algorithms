print ("******************************************************")
print ("****************Welcome to my app*********************")
print ("****************passwords manager*********************")
print ("******************************************************\n")

print ("enter your choice: ")
print ("1. Create a new user")
print ("2. View all users")


q = int(input("your choice: "))

if q == 1:

    username1 = str(input("Enter your new username: "))
    password1 = input("Enter your new password for " + username1 + ": ")
    web1 = input("Enter the website for " + username1 + ": ")

    username2 = str(input("Enter your new username: "))
    password2 = input("Enter your new password for " + username2 + ": ")
    web1 = input("Enter the website for " + username2 + ": ")

    username3 = str(input("Enter your new username: "))
    password3 = input("Enter your new password for " + username3 + ": ")
    web1 = input("Enter the website for " + username3 + ": ")






if q == 2:
    print ("1. choose a user to view: ")
    print ("2. view all users info")
    v = int(input("enter your choice: "))

    if v == "1":
        print ("1. " ,username1)
        print ("2. " ,username2)
        print ("3. " ,username3)

        inn = int(input("enter the number of the user you want to view: "))
        if inn == "1":
            print ("username: " ,username1)
            print ("password: " ,password1)
            print ("website: " ,web1)

        elif inn == "2":
            
            print ("username: " ,username2)
            print ("password: " ,password2)
            print ("website: " ,web2)

        elif inn == "3":
            print ("username: " ,username3)
            print ("password: " ,password3)
            print ("website: " ,web3)

        else :
            print ("invalid choice... try again.")

    elif v == "2":
        print ("username: " ,username1)
        print ("username: " ,username2)
        print ("username: " ,username3)

    else :
        print ("invalid choice... try again.")

else :
    print ("invalid choice... try again.")